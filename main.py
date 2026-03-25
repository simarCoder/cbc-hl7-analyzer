from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,QDialog, QVBoxLayout, QLineEdit, QPushButton, QLabel)
import sys
from ui_interface import Ui_window
from PySide6.QtCore import QThread, Signal, Slot, QDate, QDateTime, Qt
from PySide6.QtGui import QIcon
import socket
import parserModule
from enum import Enum, auto
import database 
import excel_manager
from datetime import datetime
import licenseManager
from loginWindow import Ui_loginDialog
from configWindow import Ui_mchn_Config
import json
import os




# config manager
class ConfigManager:
    def __init__(self, filepath = "config.json"):
        self.filepath = filepath
        self.defaultConfig = {"ip" : "192.168.62.79", "port" : "8080" }

    def loadConfig(self):
        if not os.path.exists(self.filepath):
            self.saveConfig(self.defaultConfig)
            return self.defaultConfig
        try:
            with open(self.filepath, "r") as f:
                return json.load(f)
        except:
            return self.defaultConfig
        
    def saveConfig(self, configData):
        with open(self.filepath, "w") as f:
            json.dump(configData, f)


#------CONFIGURATION DIALOG-------

class ConfigDialog(QDialog, Ui_mchn_Config):
    def __init__(self, configMgr, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon("Nova_sol.png"))
        self.configMgr = configMgr
        currentCfg = self.configMgr.loadConfig()
        self.ip_addr_box.setText(currentCfg.get("ip", ""))
        self.port_no_box.setText(currentCfg.get("port", ""))

        #connect buttons
        self.confirm_btn.clicked.connect(self.saveSettings)
        self.cance_btn.clicked.connect(self.reject)

    def saveSettings(self):
         IP = self.ip_addr_box.text().strip()
         PORT = self.port_no_box.text().strip()

         if not IP or not PORT:
             QMessageBox.warning(self, "ERROR", "IP and PORT cannot be empty")
             return
         
         newConfig = {"ip": IP, "port" : PORT}
         self.configMgr.saveConfig(newConfig)
         QMessageBox.information(self, "Success", "Cofiguration Saved. \nServer will restaret with new settings.")
         self.accept()





class LoginDialog(QDialog, Ui_loginDialog):
    def __init__(self):
        super().__init__()
        self.licMngr = licenseManager.LicenseManager()
        self.setWindowTitle("LOGIN WINDOW")
        self.setWindowIcon(QIcon("Nova_sol.png"))
        self.setupUi(self)
        self.login_ui = Ui_loginDialog()
        self.passwordBox.setEchoMode(QLineEdit.EchoMode.Password)
        self.versionBox.setEnabled(False)
        #connect button
        self.okBtn.clicked.connect(self.checkLogin)
        self.cancelBtn.clicked.connect(self.reject)

        #show expiry status
        expiryStr = self.licMngr.getExpiryDate()
        self.statusLabel = QLabel(f"License valid until: {expiryStr}")
        self.statusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Attempt to add it to the bottom of the dialog's layout
        if self.layout():
            self.layout().addWidget(self.statusLabel)
        
        

    def mouseDoubleClickEvent(self, event):
        #---Auto fill credits---
        self.usernameBox.setText("admin")
        self.passwordBox.setText("admin")

    def checkLogin(self):
        username = self.usernameBox.text()
        password = self.passwordBox.text()

        #----HIDDEN ADMIN COMMAND TO UPDATE LICENSE----
        if username == "admin" and password.startswith("UPDATE_LICENSE_"):
            try:
                newDate = password.replace("UPDATE_LICENSE_", "")
                datetime.strptime(newDate, "%Y-%m-%d") #Validate format
                self.licMngr.updateLicense(newDate)
                QMessageBox.information(self, "Success", f"License extended to {newDate}.\nPlease restart app.")
                sys.exit()
            except ValueError:
                QMessageBox.warning(self, "Error", "Invalid Date Format. Use YYYY-MM-DD")
                return
            
        #--NORMAL LOGIN--
        if username == "admin" and password == "admin":
            #CHECK LICENSE STATUS
            status = self.licMngr.validate()
            if status == "VALID":
                self.accept()
            elif status == "MISSING":
                QMessageBox.critical(self, "License Error",
                                        "License File is MISSING.\n\n"
                                        "Please contact the administrator for a valid license key.")
                sys.exit()
            elif status == "CLOCK_ERROR":
                QMessageBox.critical(self, "System Error",
                                        "System Date/Time is invalid (Backdated).\n\n"
                                        "Please correct your computer's date and time, or contact admin.")
                sys.exit()
            elif status == "EXPIRED":
                QMessageBox.critical(self, "license Expired",
                                        "Software License has EXPIRED.\n\n"
                                        "Please contact the administrator for renewal.")
                sys.exit()
            else: #corrupt
                QMessageBox.critical(self, "License Error",
                                        "License file is CORRUPT.\nContact administrator.")
                sys.exit()
        else:
            QMessageBox.warning(self, "Error", "Invalid Username or Password")




class UIMode(Enum):
    VIEW = auto()
    EDIT = auto()

class serverStart(QThread):
    log_signal = Signal(str)
    data_signal = Signal(dict)
    status_signal = Signal(bool)

    def __init__(self, IP, PORT):
        super().__init__()
        self.running = True
        self.ip = IP
        self.port = int(PORT)

    def stop(self):
        self.running = False

    def run(self):
        HOST = "192.168.62.79"
        PORT = 8080
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.settimeout(1.0)
        try:
            server.bind((self.ip, self.port))
            server.listen(1)
            print("Server listening")
            while self.running:
                try:
                    client, addr = server.accept()
                    self.status_signal.emit(True)
                    client.settimeout(1.0)
                    buffer = b""
                    while self.running:
                        try:
                            data = client.recv(4096)
                            if not data: break
                            buffer += data
                            while b'\x1c' in buffer:
                                msg, buffer = buffer.split(b'\x1c', 1)
                                raw = msg.decode(errors="ignore")
                                parsed = parserModule.parse_hl7_data(raw)
                                print("RAW DATA RECEIVED:\n", raw)
                                self.data_signal.emit(parsed)
                        except socket.timeout: continue
                    client.close()
                    self.status_signal.emit(False)
                except socket.timeout: continue
        finally:
            server.close()
            self.status_signal.emit(False)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_window()
        self.ui.setupUi(self)
        self.uiMode = UIMode.VIEW
        # self.setWindowIcon(QIcon("gui_components\operon.png"))
        self.configMgr = ConfigManager()
        
        self.db = database.DatabaseManager()
        self.excel_gen = excel_manager.ExcelReport()
        
        self.current_record_id = None 
        self.current_table = None 
        self.current_data = {}
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMaximum(100)
        self.ui.progressBar.setTextVisible(True)
        self.ui.progressBar.setStyleSheet("""
                QProgressBar {
                    border: 1px solid #999;
                    border-radius: 5px;
                    text-align: center;
                }
                QProgressBar::chunk {
                    background-color: #4CAF50;
                }
        """)






        if hasattr(self.ui, 'regDate_edit'):
            self.ui.regDate_edit.setDate(QDate.currentDate())

        if hasattr(self.ui, 'reptPrintDate_edit'):
            self.ui.reptPrintDate_edit.setDateTime(QDateTime.currentDateTime())

        if hasattr(self.ui, 'smplTestDate_edit'):
            self.ui.smplTestDate_edit.setDateTime(QDateTime.currentDateTime())
    


        if hasattr(self.ui, 'ref_by_box'):
            self.ui.ref_by_box.setEditable(True)
            self.ui.ref_by_box.setInsertPolicy(self.ui.ref_by_box.InsertPolicy.NoInsert)
            self.refreshDoctorList()
            self.ui.ref_by_box.setCurrentText("SELF")

        # --- UI MAPPINGS ---
        self.ui_mappings = [
            (self.ui.RBC_val, self.ui.RBC_ref, 'RBC', 'RBC'),
            (self.ui.HGB_val, self.ui.HGB_ref, 'RBC', 'HGB'),
            (self.ui.HCT_val, self.ui.HCT_ref, 'RBC', 'HCT'),
            (self.ui.MCV_val, self.ui.MCV_ref, 'RBC', 'MCV'),
            (self.ui.MCH_val, self.ui.MCH_ref, 'RBC', 'MCH'),
            (self.ui.MCHC_val, self.ui.MCHC_ref, 'RBC', 'MCHC'),
            (self.ui.RDW_CV_val, self.ui.RDW_CV_ref, 'RBC', 'RDW-CV'),
            (self.ui.RDW_SD_val, self.ui.RDW_SD_ref, 'RBC', 'RDW-SD'),

            (self.ui.WBC_val, self.ui.WBC_ref, 'WBC', 'WBC'),
            (self.ui.NEU_per_val, self.ui.NEU_per_ref, 'WBC', 'NEU%'),
            (self.ui.LYM_per_val, self.ui.LYM_per_ref, 'WBC', 'LYM%'),
            (self.ui.MON_per_val, self.ui.MON_per_ref, 'WBC', 'MON%'),
            (self.ui.EOS_per_val, self.ui.EOS_per_ref, 'WBC', 'EOS%'),
            (self.ui.BAS_per_val, self.ui.BAS_per_ref, 'WBC', 'BAS%'),

            (self.ui.NEU_hash_val, self.ui.NEU_hash_ref, 'WBC_ABSOLUTE', 'NEU#'),
            (self.ui.LYM_hash_val, self.ui.LYM_hash_ref, 'WBC_ABSOLUTE', 'LYM#'),
            (self.ui.MON_hash_val, self.ui.MON_hash_ref, 'WBC_ABSOLUTE', 'MON#'),
            (self.ui.EOS_hash_val, self.ui.EOS_hash_ref, 'WBC_ABSOLUTE', 'EOS#'),
            (self.ui.BAS_hash_val, self.ui.BAS_hash_ref, 'WBC_ABSOLUTE', 'BAS#'),

            (self.ui.PLT_val, self.ui.PLT_ref, 'PLATELET', 'PLT'),
            (self.ui.MPV_val, self.ui.MPV_ref, 'PLATELET', 'MPV'),
            (self.ui.PDW_CV_val, self.ui.PDW_CV_ref, 'PLATELET', 'PDW-CV'),
            (self.ui.PDW_SD_val, self.ui.PDW_SD_ref, 'PLATELET', 'PDW-SD'),
            (self.ui.PCT_val, self.ui.PCT_ref, 'PLATELET', 'PCT'),
            (self.ui.P_LCR_val, self.ui.P_LCR_ref, 'PLATELET', 'P-LCR'),
            (self.ui.P_LCC_val, self.ui.P_LCC_ref, 'PLATELET', 'P-LCC'),
        ]

        now = datetime.now()
        last_id, table_name = self.db.get_last_id_in_month(now)
        if last_id:
            self.load_record(last_id, table_name)
        else:
            self.current_table = table_name
            self.ui.regDateBox.setDateTime(QDateTime.currentDateTime())

        # self.worker = serverStart()
        # self.worker.data_signal.connect(self.handle_new_data)
        # self.worker.start()
        self.startServerThread()

        self.applyUiState()
        self.ui.edit_btn.clicked.connect(self.edit_mode)
        self.ui.save_btn.clicked.connect(self.save_and_disable_editing)
        self.ui.Machine_conn_check.setEnabled(False)
        
        # Navigation connections
        # try: self.ui.prev_btn.clicked.disconnect() 
        # except: pass
        self.ui.prev_btn.clicked.connect(self.on_prev_clicked)
        self.ui.next_btn.clicked.connect(self.on_next_clicked)
        
        # Report connections
        self.ui.excel_btn.clicked.connect(self.generate_excel)
        self.ui.pdf_btn.clicked.connect(self.generate_pdf_report)
        self.ui.print_btn.clicked.connect(self.printReports)

        self.ui.config_btn.clicked.connect(self.openConfigDialog)


    @Slot(bool)
    def updateMachineStatus(self, connected):
        if connected:
            self.ui.Machine_conn_check.setChecked(True)
            self.ui.progressBar.setValue(0)
        else:
            self.ui.Machine_conn_check.setChecked(False)
            self.ui.progressBar.setValue(0)




    def startServerThread(self):
        """helper to start/restart server thread with current config"""
        
        CFG = self.configMgr.loadConfig()
        #initialize the worker with IP/PORT from config
        self.worker = serverStart(CFG["ip"], CFG["port"])
        self.worker.data_signal.connect(self.handle_new_data)
        self.worker.start()
        self.worker.status_signal.connect(self.updateMachineStatus)

    def openConfigDialog(self):
        """Opens the settings Window"""
        Dlg = ConfigDialog(self.configMgr, self)
        if Dlg.exec() == QDialog.DialogCode.Accepted:
            #if saved, restarts the server with new settings
            print("Restarting server with new settings")
            if self.worker.isRunning():
                self.worker.stop()
                self.worker.wait()
            self.startServerThread()


    def closeEvent(self, event):
        if self.worker.isRunning():
            self.worker.stop()
            self.worker.wait()
        event.accept()

    def refreshDoctorList(self):
        if not hasattr(self.ui, 'ref_by_box'): return
        currentText = self.ui.ref_by_box.currentText()
        doctors = self.db.get_all_doctors()
        self.ui.ref_by_box.clear()
        self.ui.ref_by_box.addItems(doctors)
        if currentText:
            self.ui.ref_by_box.setCurrentText(currentText)
        else:
            self.ui.ref_by_box.setCurrentText("SELF")


    def applyUiState(self):
        header_widgets = [self.ui.gender_combo_box, self.ui.PID_box, self.ui.Name_box, 
                          self.ui.Age_box, self.ui.Report_no_box, self.ui.regDateBox]
        
        if hasattr(self.ui, 'ref_by_box'): header_widgets.append(self.ui.ref_by_box)
        if hasattr(self.ui, 'regDateBox'): header_widgets.append(self.ui.regDateBox)
        if hasattr(self.ui, 'smplTestD_Box'): header_widgets.append(self.ui.smplTestD_Box)
        if hasattr(self.ui, 'reptPrintD_box'): header_widgets.append(self.ui.reptPrintD_box)
        if hasattr(self.ui, 'sampleTypeBox'): header_widgets.append(self.ui.sampleTypeBox) # assuming widget name




        all_widgets = header_widgets.copy()
        for val_w, unit_w, _, _ in self.ui_mappings:
            if val_w: all_widgets.append(val_w)
            if unit_w: all_widgets.append(unit_w)

        if self.uiMode == UIMode.VIEW:
            for w in all_widgets: w.setEnabled(False)
            self.ui.save_btn.setEnabled(False)
            self.ui.cancel_btn.setEnabled(False)
            self.ui.edit_btn.setEnabled(True)
            self.ui.config_btn.setEnabled(True)

        if self.uiMode == UIMode.EDIT:
            for w in all_widgets: w.setEnabled(True)
            self.ui.save_btn.setEnabled(True)
            self.ui.cancel_btn.setEnabled(True)
            self.ui.edit_btn.setEnabled(False)
            self.ui.Name_box.setReadOnly(False)
            self.ui.config_btn.setEnabled(True)

    @Slot(dict)
    def handle_new_data(self, data):
        self.ui.progressBar.setValue(0)
        print("Received Data. Saving...")
        self.ui.progressBar.setValue(20)

        new_id, table_name, timestamp = self.db.add_record(data)
        self.ui.progressBar.setValue(40)

        self.current_record_id = new_id
        self.ui.progressBar.setValue(60)

        self.current_table = table_name
        self.ui.progressBar.setValue(80)

        self.populate_ui(data, timestamp)
        self.ui.progressBar.setValue(100)

    def load_record(self, record_id, table_name):
        data, dateStr = self.db.get_record(record_id, table_name)
        if data:
            self.current_record_id = record_id
            self.current_table = table_name
            self.populate_ui(data, dateStr)
        else:
            print(f"Record {record_id} not found.")

    def on_prev_clicked(self):
        if self.current_record_id is None or self.current_table is None: return
        prev_id = self.db.get_prev_id(self.current_record_id, self.current_table)
        if prev_id: self.load_record(prev_id, self.current_table)
        else: QMessageBox.information(self, "Info", "No previous records.")

    def on_next_clicked(self):
        if self.current_record_id is None or self.current_table is None: return
        next_id = self.db.get_next_id(self.current_record_id, self.current_table)
        if next_id: self.load_record(next_id, self.current_table)
        else: QMessageBox.information(self, "Info", "No more records.")

    def setDateWidget(self, widget, dateStr):
        if not widget or not dateStr: return
        try:
            dt = datetime.strptime(str(dateStr), "%Y-%m-%d %I:%M:%S %p")
            widget.setDateTime(dt)
        except ValueError:
            pass




    def populate_ui(self, data, date_val=None):
        """LOADS DATA FROM DICT TO SCREEN"""
        self.current_data = data
        
        self.ui.Name_box.setText(data.get('PATIENT', ''))
        self.ui.Age_box.setText(data.get('AGE', ''))
        self.ui.PID_box.setText(data.get('PATIENT_ID', ''))
        
        # --- HERE IS THE GENDER LOADING LOGIC ---
        # Forces the combo box to show the saved gender
        gender = data.get('GENDER', 'Male') # Default to Male if empty
        self.ui.gender_combo_box.setCurrentText(gender)
        

        if hasattr(self.ui, 'ref_by_box'):
            docName = data.get('REF_BY', 'SELF')
            self.ui.ref_by_box.setCurrentText(docName)
            self.current_data['REF_BY'] = docName


        if hasattr(self.ui, 'regDateBox'):
            # Reg Date is often current time if not in data, or parsed data
            reg = data.get('REG_DATE', datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"))
            self.setDateWidget(self.ui.regDateBox, reg)
            self.current_data['REG_DATE'] = reg # Ensure in data for PDF

        if hasattr(self.ui, 'smplTestD_Box'):
            smpl = data.get('SAMPLE_DATE', '')
            self.setDateWidget(self.ui.smplTestD_Box, smpl)
            self.current_data['SAMPLE_DATE'] = smpl

        if hasattr(self.ui, 'reptPrintD_box'):
            # Default to now if empty, or load saved
            rpt = data.get('REPORT_DATE', datetime.now().strftime("%Y-%m-%d %I:%M:%S %p"))
            self.setDateWidget(self.ui.reptPrintD_box, rpt)
            self.current_data['REPORT_DATE'] = rpt

        if hasattr(self.ui, 'sampleTypeBox'):
            val = data.get('SAMPLE_TYPE', 'Whole Blood')
            if isinstance(self.ui.sampleTypeBox, QLineEdit):
                self.ui.sampleTypeBox.setText(val)
            else:
                self.ui.sampleTypeBox.setCurrentText(val)
            self.current_data['SAMPLE_TYPE'] = val





        if self.current_record_id:
            self.ui.Report_no_box.setText(str(self.current_record_id))

        if date_val:
            if isinstance(date_val, str):
                try: self.ui.regDateBox.setDateTime(datetime.fromisoformat(date_val))
                except: pass
            elif isinstance(date_val, datetime):
                self.ui.regDateBox.setDateTime(date_val)

        for val_widget, unit_widget, section, test_name in self.ui_mappings:
            try:
                item = data.get(section, {}).get(test_name, {})
                if val_widget: val_widget.setText(str(item.get('value', '')))
                if unit_widget: unit_widget.setText(str(item.get('unit', '')))
            except: pass

    def edit_mode(self):
        self.uiMode = UIMode.EDIT
        self.applyUiState()

    def save_and_disable_editing(self):
        """SCRAPES DATA FROM SCREEN TO DATABASE"""
        if not self.current_record_id or not self.current_table:
            return

        print("Saving changes to database...")

        #images logic
        existing_images = self.current_data.get("IMAGES", {})

        self.current_data['PATIENT'] = self.ui.Name_box.text()
        self.current_data['AGE'] = self.ui.Age_box.text()
        self.current_data['PATIENT_ID'] = self.ui.PID_box.text()
        
        # --- HERE IS THE GENDER SAVING LOGIC ---
        # Gets the currently selected text from the combobox
        self.current_data['GENDER'] = self.ui.gender_combo_box.currentText()

        if hasattr(self.ui, 'ref_by_box'):
            docName = self.ui.ref_by_box.currentText().strip().upper()
            if not docName: docName = "SELF"
            self.current_data['REF_BY'] = docName
            if self.db.add_doctor(docName):
                self.refreshDoctorList()
                self.ui.ref_by_box.setCurrentText(docName)

        self.current_data['IMAGES'] = existing_images

        for val_widget, unit_widget, section, test_name in self.ui_mappings:
            if section not in self.current_data:
                self.current_data[section] = {}
            if test_name not in self.current_data[section]:
                self.current_data[section][test_name] = {}
            
            if val_widget:
                self.current_data[section][test_name]['value'] = val_widget.text()
            if unit_widget:
                self.current_data[section][test_name]['unit'] = unit_widget.text()

        self.db.update_record(self.current_record_id, self.current_table, self.current_data)
        self.uiMode = UIMode.VIEW
        self.applyUiState()
        QMessageBox.information(self, "Success", "Record Updated.")

    def _scrape_current_state(self):
        """Helper to ensure we print what is on screen, even if not saved."""
        if not self.current_data: return
        self.current_data['PATIENT'] = self.ui.Name_box.text()
        self.current_data['AGE'] = self.ui.Age_box.text()
        self.current_data['PATIENT_ID'] = self.ui.PID_box.text()
        # Ensure we capture gender for printing
        self.current_data['GENDER'] = self.ui.gender_combo_box.currentText()
        # Note: We aren't scraping values here for brevity, assumes saved or loaded.
        # Ideally, this should loop through ui_mappings too if you edit values without saving.
        if hasattr(self.ui, 'ref_by_box'):
            self.current_data['REF_BY'] = self.ui.ref_by_box.currentText()


        if hasattr(self.ui, 'regDateBox'):
            self.current_data['REG_DATE'] = self.ui.regDateBox.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        if hasattr(self.ui, 'smplTestD_Box'):
            self.current_data['SAMPLE_DATE'] = self.ui.smplTestD_Box.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        if hasattr(self.ui, 'reptPrintD_box'):
            self.current_data['REPORT_DATE'] = self.ui.reptPrintD_box.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        if hasattr(self.ui, 'sampleTypeBox'):
            # Check if it's LineEdit or ComboBox in your UI
            if isinstance(self.ui.sampleTypeBox, QLineEdit):
                self.current_data['SAMPLE_TYPE'] = self.ui.sampleTypeBox.text()
            else:
                self.current_data['SAMPLE_TYPE'] = self.ui.sampleTypeBox.currentText()
            

    def _update_print_date(self):
        """Updates Report Date to NOW before printing."""
        now_str = datetime.now().strftime("%Y-%m-%d/%I:%M %p")
        if hasattr(self.ui, 'reptPrintD_box'):
            self.ui.reptPrintD_box.setDateTime(QDateTime.currentDateTime())
        self.current_data['REPORT_DATE'] = now_str

    def generate_excel(self):
        if not self.current_data:
            QMessageBox.warning(self, "Warning", "No data loaded!")
            return

        # Ensure we have the latest gender/name if user didn't click save
        if self.uiMode == UIMode.VIEW:
             self._scrape_current_state()
             self._update_print_date()
        
        success = self.excel_gen.generate(self.current_data)
        if success:
            self.excel_gen.open_file()
        else:
            QMessageBox.critical(self, "Error", "Could not generate Excel report. Close the excel file")

    def generate_pdf_report(self):
        if not self.current_data:
            QMessageBox.warning(self, "Warning", "No data loaded!")
            return
            
        if self.uiMode == UIMode.EDIT:
            self._scrape_current_state()
            self._update_print_date()

        print("Generating PDF...")
        QApplication.setOverrideCursor(sys.modules['PySide6.QtCore'].Qt.WaitCursor)
        
        success, result_msg = self.excel_gen.save_as_pdf(self.current_data)
        
        QApplication.restoreOverrideCursor()
        
        if success:
            self.excel_gen.open_pdf_folder()
            QMessageBox.information(self, "Success", f"PDF Saved.")
        else:
            QMessageBox.critical(self, "Error", f"PDF Generation Failed:\n{result_msg}")


    def printReports(self):
        if not self.current_data:
            QMessageBox.warning(self, "Warning", "No data loaded to print!")
            return
        if self.uiMode == UIMode.VIEW:
            self._scrape_current_state()
            self._update_print_date()

        print("Sending to Printer...")
        QApplication.setOverrideCursor(sys.modules['PySide6.QtCore'].Qt.WaitCursor)
        success, msg = self.excel_gen.print_file(self.current_data)
        QApplication.restoreOverrideCursor()

        if success:
            QMessageBox.information(self, "Success", "Document sent to printer.")
        else:
            QMessageBox.critical(self, "Print Error", f"Failed to print:\n {msg}")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginDialog()
    if login.exec() == QDialog.DialogCode.Accepted:
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit()

#UPDATE_LICENSE_2026-03-26
