# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDateTimeEdit, QFormLayout, QFrame, QGridLayout,
    QLabel, QLineEdit, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_window(object):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(791, 506)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(255, 246, 238, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        brush3 = QBrush(QColor(255, 250, 246, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush3)
        brush4 = QBrush(QColor(127, 123, 119, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush4)
        brush5 = QBrush(QColor(170, 164, 159, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush2)
        brush6 = QBrush(QColor(237, 238, 255, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush6)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush3)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 128))
        brush8.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush6)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush3)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush6)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush6)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        window.setPalette(palette)
        window.setAutoFillBackground(True)
        self.gridLayoutWidget = QWidget(window)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 725, 30))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.prev_btn = QPushButton(self.gridLayoutWidget)
        self.prev_btn.setObjectName(u"prev_btn")
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush9 = QBrush(QColor(191, 204, 240, 255))
        brush9.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush9)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        brush10 = QBrush(QColor(237, 255, 238, 255))
        brush10.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush10)
        brush11 = QBrush(QColor(109, 127, 110, 255))
        brush11.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush11)
        brush12 = QBrush(QColor(146, 170, 147, 255))
        brush12.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush12)
        brush13 = QBrush(QColor(244, 242, 213, 255))
        brush13.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush13)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        brush14 = QBrush(QColor(7, 7, 6, 255))
        brush14.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush14)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush9)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
        brush15 = QBrush(QColor(244, 242, 213, 128))
        brush15.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush9)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush10)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush11)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush12)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush13)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush14)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush9)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush9)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush9)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush10)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush11)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush12)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        brush16 = QBrush(QColor(219, 255, 221, 255))
        brush16.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush16)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        self.prev_btn.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"Candara"])
        font.setPointSize(9)
        font.setBold(True)
        self.prev_btn.setFont(font)
        self.prev_btn.setStyleSheet(u"background-color: #bfccf0;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.prev_btn, 0, 2, 1, 1)

        self.print_btn = QPushButton(self.gridLayoutWidget)
        self.print_btn.setObjectName(u"print_btn")
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush9)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush10)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush11)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush12)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush13)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush14)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush9)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush9)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush10)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush11)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush12)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush13)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush14)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush9)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush9)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush9)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush10)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush11)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush12)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush16)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        self.print_btn.setPalette(palette2)
        self.print_btn.setFont(font)
        self.print_btn.setStyleSheet(u"background-color: #bfccf0;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.print_btn, 0, 7, 1, 1)

        self.edit_btn = QPushButton(self.gridLayoutWidget)
        self.edit_btn.setObjectName(u"edit_btn")
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush9)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush10)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush11)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush12)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush13)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush14)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush9)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush9)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush10)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush11)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush12)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush13)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush14)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush9)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush9)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush9)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush10)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush11)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush12)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush16)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        self.edit_btn.setPalette(palette3)
        self.edit_btn.setFont(font)
        self.edit_btn.setStyleSheet(u"background-color: #bfccf0;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.edit_btn, 0, 4, 1, 1)

        self.excel_btn = QPushButton(self.gridLayoutWidget)
        self.excel_btn.setObjectName(u"excel_btn")
        palette4 = QPalette()
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush9)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush10)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush11)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush12)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush13)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush14)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush9)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush9)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush10)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush11)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush12)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush13)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush14)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush9)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush9)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush9)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush10)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush11)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush12)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush16)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        self.excel_btn.setPalette(palette4)
        self.excel_btn.setFont(font)
        self.excel_btn.setStyleSheet(u"background-color: #bfccf0;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.excel_btn, 0, 6, 1, 1)

        self.save_btn = QPushButton(self.gridLayoutWidget)
        self.save_btn.setObjectName(u"save_btn")
        palette5 = QPalette()
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush9)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush10)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush11)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush12)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush13)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush14)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush9)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush9)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush10)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush11)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush12)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush13)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush14)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush9)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush9)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush9)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush10)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush11)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush12)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush16)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        self.save_btn.setPalette(palette5)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet(u"background-color: #bfccf0;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.save_btn, 0, 0, 1, 1)

        self.pdf_btn = QPushButton(self.gridLayoutWidget)
        self.pdf_btn.setObjectName(u"pdf_btn")
        palette6 = QPalette()
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush9)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush10)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush11)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush12)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush13)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush14)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush9)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush9)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush10)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush11)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush12)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush13)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush14)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush9)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush9)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush9)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush10)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush11)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush12)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush16)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        self.pdf_btn.setPalette(palette6)
        self.pdf_btn.setFont(font)
        self.pdf_btn.setStyleSheet(u"background-color: #bfccf0;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.pdf_btn, 0, 5, 1, 1)

        self.next_btn = QPushButton(self.gridLayoutWidget)
        self.next_btn.setObjectName(u"next_btn")
        palette7 = QPalette()
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush9)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush10)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush11)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush12)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush13)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush14)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush9)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush9)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush10)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush11)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush12)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush13)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush14)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush9)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush9)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush9)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush10)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush11)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush12)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush16)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        self.next_btn.setPalette(palette7)
        self.next_btn.setFont(font)
        self.next_btn.setStyleSheet(u"background-color: #bfccf0;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.next_btn, 0, 3, 1, 1)

        self.config_btn = QPushButton(self.gridLayoutWidget)
        self.config_btn.setObjectName(u"config_btn")
        palette8 = QPalette()
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush9)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush10)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush11)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush12)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush13)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush14)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush9)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush9)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush10)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush11)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush12)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush13)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush14)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush9)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush9)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush9)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush10)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush11)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush12)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush16)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette8.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        self.config_btn.setPalette(palette8)
        self.config_btn.setFont(font)
        self.config_btn.setStyleSheet(u"background-color: #bfccf0;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.config_btn, 0, 8, 1, 1)

        self.cancel_btn = QPushButton(self.gridLayoutWidget)
        self.cancel_btn.setObjectName(u"cancel_btn")
        palette9 = QPalette()
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush9)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush2)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush10)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush11)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush12)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush13)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, brush2)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush14)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush9)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, brush)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, brush10)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush7)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush9)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush2)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, brush10)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, brush11)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, brush12)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush13)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, brush2)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush14)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush9)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush9)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, brush)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, brush10)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush7)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush11)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush9)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush2)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, brush10)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, brush11)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, brush12)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush11)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, brush2)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush11)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush9)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush9)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, brush)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, brush16)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, brush7)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette9.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush8)
#endif
        self.cancel_btn.setPalette(palette9)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet(u"background-color: #bfccf0;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.cancel_btn, 0, 1, 1, 1)

        self.formLayoutWidget = QWidget(window)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 160, 111, 248))
        self.RBC_layout = QFormLayout(self.formLayoutWidget)
        self.RBC_layout.setObjectName(u"RBC_layout")
        self.RBC_layout.setContentsMargins(0, 0, 0, 0)
        self.rBCLabel = QLabel(self.formLayoutWidget)
        self.rBCLabel.setObjectName(u"rBCLabel")
        font1 = QFont()
        font1.setFamilies([u"Constantia"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.rBCLabel.setFont(font1)

        self.RBC_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.rBCLabel)

        self.hGBLabel = QLabel(self.formLayoutWidget)
        self.hGBLabel.setObjectName(u"hGBLabel")
        self.hGBLabel.setFont(font1)

        self.RBC_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.hGBLabel)

        self.hCTLabel = QLabel(self.formLayoutWidget)
        self.hCTLabel.setObjectName(u"hCTLabel")
        self.hCTLabel.setFont(font1)

        self.RBC_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.hCTLabel)

        self.HCT_val = QLineEdit(self.formLayoutWidget)
        self.HCT_val.setObjectName(u"HCT_val")
        self.HCT_val.setMaximumSize(QSize(43, 16777215))
        self.HCT_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.RBC_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.HCT_val)

        self.mCVLabel = QLabel(self.formLayoutWidget)
        self.mCVLabel.setObjectName(u"mCVLabel")
        self.mCVLabel.setFont(font1)

        self.RBC_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.mCVLabel)

        self.MCV_val = QLineEdit(self.formLayoutWidget)
        self.MCV_val.setObjectName(u"MCV_val")
        self.MCV_val.setMaximumSize(QSize(43, 16777215))
        self.MCV_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.RBC_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.MCV_val)

        self.mCHLabel = QLabel(self.formLayoutWidget)
        self.mCHLabel.setObjectName(u"mCHLabel")
        self.mCHLabel.setFont(font1)

        self.RBC_layout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.mCHLabel)

        self.MCH_val = QLineEdit(self.formLayoutWidget)
        self.MCH_val.setObjectName(u"MCH_val")
        self.MCH_val.setMaximumSize(QSize(43, 16777215))
        self.MCH_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.RBC_layout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.MCH_val)

        self.mCHCLabel = QLabel(self.formLayoutWidget)
        self.mCHCLabel.setObjectName(u"mCHCLabel")
        self.mCHCLabel.setFont(font1)

        self.RBC_layout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.mCHCLabel)

        self.MCHC_val = QLineEdit(self.formLayoutWidget)
        self.MCHC_val.setObjectName(u"MCHC_val")
        self.MCHC_val.setMaximumSize(QSize(43, 16777215))
        self.MCHC_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.RBC_layout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.MCHC_val)

        self.rDW_CVLabel = QLabel(self.formLayoutWidget)
        self.rDW_CVLabel.setObjectName(u"rDW_CVLabel")
        self.rDW_CVLabel.setFont(font1)

        self.RBC_layout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.rDW_CVLabel)

        self.RDW_CV_val = QLineEdit(self.formLayoutWidget)
        self.RDW_CV_val.setObjectName(u"RDW_CV_val")
        self.RDW_CV_val.setMaximumSize(QSize(43, 16777215))
        self.RDW_CV_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.RBC_layout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.RDW_CV_val)

        self.rDW_SDLabel = QLabel(self.formLayoutWidget)
        self.rDW_SDLabel.setObjectName(u"rDW_SDLabel")
        self.rDW_SDLabel.setFont(font1)

        self.RBC_layout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.rDW_SDLabel)

        self.RDW_SD_val = QLineEdit(self.formLayoutWidget)
        self.RDW_SD_val.setObjectName(u"RDW_SD_val")
        self.RDW_SD_val.setMaximumSize(QSize(43, 16777215))
        self.RDW_SD_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.RBC_layout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.RDW_SD_val)

        self.RBC_val = QLineEdit(self.formLayoutWidget)
        self.RBC_val.setObjectName(u"RBC_val")
        self.RBC_val.setMaximumSize(QSize(43, 16777215))
        self.RBC_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.RBC_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.RBC_val)

        self.HGB_val = QLineEdit(self.formLayoutWidget)
        self.HGB_val.setObjectName(u"HGB_val")
        self.HGB_val.setMaximumSize(QSize(43, 16777215))
        self.HGB_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.RBC_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.HGB_val)

        self.formLayoutWidget_2 = QWidget(window)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(190, 160, 88, 182))
        self.WBC_layout = QFormLayout(self.formLayoutWidget_2)
        self.WBC_layout.setObjectName(u"WBC_layout")
        self.WBC_layout.setContentsMargins(0, 0, 0, 0)
        self.WBC_val = QLineEdit(self.formLayoutWidget_2)
        self.WBC_val.setObjectName(u"WBC_val")
        self.WBC_val.setMaximumSize(QSize(40, 16777215))
        self.WBC_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.WBC_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.WBC_val)

        self.nEULabel = QLabel(self.formLayoutWidget_2)
        self.nEULabel.setObjectName(u"nEULabel")
        self.nEULabel.setFont(font1)

        self.WBC_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.nEULabel)

        self.NEU_per_val = QLineEdit(self.formLayoutWidget_2)
        self.NEU_per_val.setObjectName(u"NEU_per_val")
        self.NEU_per_val.setMaximumSize(QSize(40, 16777215))
        self.NEU_per_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.WBC_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.NEU_per_val)

        self.lYMLabel = QLabel(self.formLayoutWidget_2)
        self.lYMLabel.setObjectName(u"lYMLabel")
        self.lYMLabel.setFont(font1)

        self.WBC_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lYMLabel)

        self.LYM_per_val = QLineEdit(self.formLayoutWidget_2)
        self.LYM_per_val.setObjectName(u"LYM_per_val")
        self.LYM_per_val.setMaximumSize(QSize(40, 16777215))
        self.LYM_per_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.WBC_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.LYM_per_val)

        self.mONLabel = QLabel(self.formLayoutWidget_2)
        self.mONLabel.setObjectName(u"mONLabel")
        self.mONLabel.setFont(font1)

        self.WBC_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.mONLabel)

        self.MON_per_val = QLineEdit(self.formLayoutWidget_2)
        self.MON_per_val.setObjectName(u"MON_per_val")
        self.MON_per_val.setMaximumSize(QSize(40, 16777215))
        self.MON_per_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.WBC_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.MON_per_val)

        self.eOSLabel = QLabel(self.formLayoutWidget_2)
        self.eOSLabel.setObjectName(u"eOSLabel")
        self.eOSLabel.setFont(font1)

        self.WBC_layout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.eOSLabel)

        self.EOS_per_val = QLineEdit(self.formLayoutWidget_2)
        self.EOS_per_val.setObjectName(u"EOS_per_val")
        self.EOS_per_val.setMaximumSize(QSize(40, 16777215))
        self.EOS_per_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.WBC_layout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.EOS_per_val)

        self.bASLabel = QLabel(self.formLayoutWidget_2)
        self.bASLabel.setObjectName(u"bASLabel")
        self.bASLabel.setFont(font1)

        self.WBC_layout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.bASLabel)

        self.BAS_per_val = QLineEdit(self.formLayoutWidget_2)
        self.BAS_per_val.setObjectName(u"BAS_per_val")
        self.BAS_per_val.setMaximumSize(QSize(40, 16777215))
        self.BAS_per_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.WBC_layout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.BAS_per_val)

        self.wBCLabel = QLabel(self.formLayoutWidget_2)
        self.wBCLabel.setObjectName(u"wBCLabel")
        self.wBCLabel.setFont(font1)

        self.WBC_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.wBCLabel)

        self.formLayoutWidget_3 = QWidget(window)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(360, 160, 89, 151))
        self.Abslt_layout = QFormLayout(self.formLayoutWidget_3)
        self.Abslt_layout.setObjectName(u"Abslt_layout")
        self.Abslt_layout.setContentsMargins(0, 0, 0, 0)
        self.nEULabel_2 = QLabel(self.formLayoutWidget_3)
        self.nEULabel_2.setObjectName(u"nEULabel_2")
        self.nEULabel_2.setFont(font1)

        self.Abslt_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nEULabel_2)

        self.NEU_hash_val = QLineEdit(self.formLayoutWidget_3)
        self.NEU_hash_val.setObjectName(u"NEU_hash_val")
        self.NEU_hash_val.setMaximumSize(QSize(43, 16777215))
        self.NEU_hash_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.Abslt_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.NEU_hash_val)

        self.lYMLabel_2 = QLabel(self.formLayoutWidget_3)
        self.lYMLabel_2.setObjectName(u"lYMLabel_2")
        self.lYMLabel_2.setFont(font1)

        self.Abslt_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lYMLabel_2)

        self.LYM_hash_val = QLineEdit(self.formLayoutWidget_3)
        self.LYM_hash_val.setObjectName(u"LYM_hash_val")
        self.LYM_hash_val.setMaximumSize(QSize(43, 16777215))
        self.LYM_hash_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.Abslt_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.LYM_hash_val)

        self.mONLabel_2 = QLabel(self.formLayoutWidget_3)
        self.mONLabel_2.setObjectName(u"mONLabel_2")
        self.mONLabel_2.setFont(font1)

        self.Abslt_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.mONLabel_2)

        self.MON_hash_val = QLineEdit(self.formLayoutWidget_3)
        self.MON_hash_val.setObjectName(u"MON_hash_val")
        self.MON_hash_val.setMaximumSize(QSize(43, 16777215))
        self.MON_hash_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.Abslt_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.MON_hash_val)

        self.eOSLabel_2 = QLabel(self.formLayoutWidget_3)
        self.eOSLabel_2.setObjectName(u"eOSLabel_2")
        self.eOSLabel_2.setFont(font1)

        self.Abslt_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.eOSLabel_2)

        self.EOS_hash_val = QLineEdit(self.formLayoutWidget_3)
        self.EOS_hash_val.setObjectName(u"EOS_hash_val")
        self.EOS_hash_val.setMaximumSize(QSize(43, 16777215))
        self.EOS_hash_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.Abslt_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.EOS_hash_val)

        self.bASLabel_2 = QLabel(self.formLayoutWidget_3)
        self.bASLabel_2.setObjectName(u"bASLabel_2")
        self.bASLabel_2.setFont(font1)

        self.Abslt_layout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.bASLabel_2)

        self.BAS_hash_val = QLineEdit(self.formLayoutWidget_3)
        self.BAS_hash_val.setObjectName(u"BAS_hash_val")
        self.BAS_hash_val.setMaximumSize(QSize(43, 16777215))
        self.BAS_hash_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.Abslt_layout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.BAS_hash_val)

        self.formLayoutWidget_4 = QWidget(window)
        self.formLayoutWidget_4.setObjectName(u"formLayoutWidget_4")
        self.formLayoutWidget_4.setGeometry(QRect(530, 160, 101, 213))
        self.Platelet_layout = QFormLayout(self.formLayoutWidget_4)
        self.Platelet_layout.setObjectName(u"Platelet_layout")
        self.Platelet_layout.setContentsMargins(0, 0, 0, 0)
        self.pLTLabel = QLabel(self.formLayoutWidget_4)
        self.pLTLabel.setObjectName(u"pLTLabel")
        self.pLTLabel.setFont(font1)

        self.Platelet_layout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pLTLabel)

        self.PLT_val = QLineEdit(self.formLayoutWidget_4)
        self.PLT_val.setObjectName(u"PLT_val")
        self.PLT_val.setMaximumSize(QSize(43, 16777215))
        self.PLT_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.Platelet_layout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.PLT_val)

        self.mPVLabel = QLabel(self.formLayoutWidget_4)
        self.mPVLabel.setObjectName(u"mPVLabel")
        self.mPVLabel.setFont(font1)

        self.Platelet_layout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.mPVLabel)

        self.MPV_val = QLineEdit(self.formLayoutWidget_4)
        self.MPV_val.setObjectName(u"MPV_val")
        self.MPV_val.setMaximumSize(QSize(43, 16777215))
        self.MPV_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.Platelet_layout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.MPV_val)

        self.pDWSDLabel = QLabel(self.formLayoutWidget_4)
        self.pDWSDLabel.setObjectName(u"pDWSDLabel")
        self.pDWSDLabel.setFont(font1)

        self.Platelet_layout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.pDWSDLabel)

        self.PDW_SD_val = QLineEdit(self.formLayoutWidget_4)
        self.PDW_SD_val.setObjectName(u"PDW_SD_val")
        self.PDW_SD_val.setMaximumSize(QSize(43, 16777215))
        self.PDW_SD_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.Platelet_layout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.PDW_SD_val)

        self.pDWCVLabel = QLabel(self.formLayoutWidget_4)
        self.pDWCVLabel.setObjectName(u"pDWCVLabel")
        self.pDWCVLabel.setFont(font1)

        self.Platelet_layout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.pDWCVLabel)

        self.PDW_CV_val = QLineEdit(self.formLayoutWidget_4)
        self.PDW_CV_val.setObjectName(u"PDW_CV_val")
        self.PDW_CV_val.setMaximumSize(QSize(43, 16777215))
        self.PDW_CV_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.Platelet_layout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.PDW_CV_val)

        self.pCTLabel = QLabel(self.formLayoutWidget_4)
        self.pCTLabel.setObjectName(u"pCTLabel")
        self.pCTLabel.setFont(font1)

        self.Platelet_layout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.pCTLabel)

        self.PCT_val = QLineEdit(self.formLayoutWidget_4)
        self.PCT_val.setObjectName(u"PCT_val")
        self.PCT_val.setMaximumSize(QSize(43, 16777215))
        self.PCT_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.Platelet_layout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.PCT_val)

        self.pLCRLabel = QLabel(self.formLayoutWidget_4)
        self.pLCRLabel.setObjectName(u"pLCRLabel")
        self.pLCRLabel.setFont(font1)

        self.Platelet_layout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.pLCRLabel)

        self.P_LCR_val = QLineEdit(self.formLayoutWidget_4)
        self.P_LCR_val.setObjectName(u"P_LCR_val")
        self.P_LCR_val.setMaximumSize(QSize(43, 16777215))
        self.P_LCR_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.Platelet_layout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.P_LCR_val)

        self.pLCCLabel = QLabel(self.formLayoutWidget_4)
        self.pLCCLabel.setObjectName(u"pLCCLabel")
        self.pLCCLabel.setFont(font1)

        self.Platelet_layout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.pLCCLabel)

        self.P_LCC_val = QLineEdit(self.formLayoutWidget_4)
        self.P_LCC_val.setObjectName(u"P_LCC_val")
        self.P_LCC_val.setMaximumSize(QSize(43, 16777215))
        self.P_LCC_val.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.Platelet_layout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.P_LCC_val)

        self.verticalLayoutWidget = QWidget(window)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(120, 160, 61, 244))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MCH_ref = QLineEdit(self.verticalLayoutWidget)
        self.MCH_ref.setObjectName(u"MCH_ref")
        self.MCH_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.MCH_ref)

        self.HGB_ref = QLineEdit(self.verticalLayoutWidget)
        self.HGB_ref.setObjectName(u"HGB_ref")
        self.HGB_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.HGB_ref)

        self.RBC_ref = QLineEdit(self.verticalLayoutWidget)
        self.RBC_ref.setObjectName(u"RBC_ref")
        self.RBC_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.RBC_ref)

        self.RDW_CV_ref = QLineEdit(self.verticalLayoutWidget)
        self.RDW_CV_ref.setObjectName(u"RDW_CV_ref")
        self.RDW_CV_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.RDW_CV_ref)

        self.HCT_ref = QLineEdit(self.verticalLayoutWidget)
        self.HCT_ref.setObjectName(u"HCT_ref")
        self.HCT_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.HCT_ref)

        self.MCHC_ref = QLineEdit(self.verticalLayoutWidget)
        self.MCHC_ref.setObjectName(u"MCHC_ref")
        self.MCHC_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.MCHC_ref)

        self.MCV_ref = QLineEdit(self.verticalLayoutWidget)
        self.MCV_ref.setObjectName(u"MCV_ref")
        self.MCV_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.MCV_ref)

        self.RDW_SD_ref = QLineEdit(self.verticalLayoutWidget)
        self.RDW_SD_ref.setObjectName(u"RDW_SD_ref")
        self.RDW_SD_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout.addWidget(self.RDW_SD_ref)

        self.verticalLayoutWidget_2 = QWidget(window)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(290, 160, 61, 182))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.WBC_ref = QLineEdit(self.verticalLayoutWidget_2)
        self.WBC_ref.setObjectName(u"WBC_ref")
        self.WBC_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_2.addWidget(self.WBC_ref)

        self.NEU_per_ref = QLineEdit(self.verticalLayoutWidget_2)
        self.NEU_per_ref.setObjectName(u"NEU_per_ref")
        self.NEU_per_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_2.addWidget(self.NEU_per_ref)

        self.LYM_per_ref = QLineEdit(self.verticalLayoutWidget_2)
        self.LYM_per_ref.setObjectName(u"LYM_per_ref")
        self.LYM_per_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_2.addWidget(self.LYM_per_ref)

        self.MON_per_ref = QLineEdit(self.verticalLayoutWidget_2)
        self.MON_per_ref.setObjectName(u"MON_per_ref")
        self.MON_per_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_2.addWidget(self.MON_per_ref)

        self.EOS_per_ref = QLineEdit(self.verticalLayoutWidget_2)
        self.EOS_per_ref.setObjectName(u"EOS_per_ref")
        self.EOS_per_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_2.addWidget(self.EOS_per_ref)

        self.BAS_per_ref = QLineEdit(self.verticalLayoutWidget_2)
        self.BAS_per_ref.setObjectName(u"BAS_per_ref")
        self.BAS_per_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_2.addWidget(self.BAS_per_ref)

        self.verticalLayoutWidget_3 = QWidget(window)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(460, 160, 61, 151))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.NEU_hash_ref = QLineEdit(self.verticalLayoutWidget_3)
        self.NEU_hash_ref.setObjectName(u"NEU_hash_ref")
        self.NEU_hash_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_3.addWidget(self.NEU_hash_ref)

        self.LYM_hash_ref = QLineEdit(self.verticalLayoutWidget_3)
        self.LYM_hash_ref.setObjectName(u"LYM_hash_ref")
        self.LYM_hash_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_3.addWidget(self.LYM_hash_ref)

        self.MON_hash_ref = QLineEdit(self.verticalLayoutWidget_3)
        self.MON_hash_ref.setObjectName(u"MON_hash_ref")
        self.MON_hash_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_3.addWidget(self.MON_hash_ref)

        self.EOS_hash_ref = QLineEdit(self.verticalLayoutWidget_3)
        self.EOS_hash_ref.setObjectName(u"EOS_hash_ref")
        self.EOS_hash_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_3.addWidget(self.EOS_hash_ref)

        self.BAS_hash_ref = QLineEdit(self.verticalLayoutWidget_3)
        self.BAS_hash_ref.setObjectName(u"BAS_hash_ref")
        self.BAS_hash_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_3.addWidget(self.BAS_hash_ref)

        self.verticalLayoutWidget_4 = QWidget(window)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(640, 160, 71, 213))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.PLT_ref = QLineEdit(self.verticalLayoutWidget_4)
        self.PLT_ref.setObjectName(u"PLT_ref")
        self.PLT_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.PLT_ref)

        self.MPV_ref = QLineEdit(self.verticalLayoutWidget_4)
        self.MPV_ref.setObjectName(u"MPV_ref")
        self.MPV_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.MPV_ref)

        self.PDW_SD_ref = QLineEdit(self.verticalLayoutWidget_4)
        self.PDW_SD_ref.setObjectName(u"PDW_SD_ref")
        self.PDW_SD_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.PDW_SD_ref)

        self.PDW_CV_ref = QLineEdit(self.verticalLayoutWidget_4)
        self.PDW_CV_ref.setObjectName(u"PDW_CV_ref")
        self.PDW_CV_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.PDW_CV_ref)

        self.PCT_ref = QLineEdit(self.verticalLayoutWidget_4)
        self.PCT_ref.setObjectName(u"PCT_ref")
        self.PCT_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.PCT_ref)

        self.P_LCR_ref = QLineEdit(self.verticalLayoutWidget_4)
        self.P_LCR_ref.setObjectName(u"P_LCR_ref")
        self.P_LCR_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.P_LCR_ref)

        self.P_LCC_ref = QLineEdit(self.verticalLayoutWidget_4)
        self.P_LCC_ref.setObjectName(u"P_LCC_ref")
        self.P_LCC_ref.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.verticalLayout_4.addWidget(self.P_LCC_ref)

        self.label = QLabel(window)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 140, 41, 16))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label_5 = QLabel(window)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 137, 41, 21))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(7)
        font3.setBold(True)
        self.label_5.setFont(font3)
        self.label_6 = QLabel(window)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 136, 41, 20))
        self.label_6.setFont(font3)
        self.label_7 = QLabel(window)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(230, 140, 41, 16))
        self.label_7.setFont(font3)
        self.label_8 = QLabel(window)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 140, 41, 16))
        self.label_8.setFont(font3)
        self.label_9 = QLabel(window)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(360, 140, 41, 16))
        self.label_9.setFont(font3)
        self.label_10 = QLabel(window)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(530, 140, 41, 16))
        self.label_10.setFont(font3)
        self.label_11 = QLabel(window)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(400, 140, 41, 16))
        self.label_11.setFont(font3)
        self.label_12 = QLabel(window)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(580, 140, 41, 16))
        self.label_12.setFont(font3)
        self.line = QFrame(window)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(109, 130, 21, 271))
        palette10 = QPalette()
        brush17 = QBrush(QColor(255, 246, 237, 255))
        brush17.setStyle(Qt.BrushStyle.SolidPattern)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush18 = QBrush(QColor(255, 246, 237, 128))
        brush18.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush18)
#endif
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush19 = QBrush(QColor(255, 246, 237, 128))
        brush19.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush19)
#endif
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush20 = QBrush(QColor(255, 246, 237, 128))
        brush20.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette10.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush20)
#endif
        self.line.setPalette(palette10)
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(window)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(176, 130, 20, 271))
        palette11 = QPalette()
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush21 = QBrush(QColor(255, 246, 237, 128))
        brush21.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush21)
#endif
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush22 = QBrush(QColor(255, 246, 237, 128))
        brush22.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush22)
#endif
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush23 = QBrush(QColor(255, 246, 237, 128))
        brush23.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette11.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush23)
#endif
        self.line_2.setPalette(palette11)
        self.line_2.setAutoFillBackground(False)
        self.line_2.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(window)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(269, 130, 31, 271))
        palette12 = QPalette()
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush24 = QBrush(QColor(255, 246, 237, 128))
        brush24.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush24)
#endif
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush25 = QBrush(QColor(255, 246, 237, 128))
        brush25.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush25)
#endif
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush26 = QBrush(QColor(255, 246, 237, 128))
        brush26.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette12.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush26)
#endif
        self.line_3.setPalette(palette12)
        self.line_3.setAutoFillBackground(False)
        self.line_3.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4 = QFrame(window)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(345, 130, 21, 271))
        palette13 = QPalette()
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush27 = QBrush(QColor(255, 246, 237, 128))
        brush27.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush27)
#endif
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush28 = QBrush(QColor(255, 246, 237, 128))
        brush28.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush28)
#endif
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush29 = QBrush(QColor(255, 246, 237, 128))
        brush29.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette13.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush29)
#endif
        self.line_4.setPalette(palette13)
        self.line_4.setAutoFillBackground(False)
        self.line_4.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_5 = QFrame(window)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(436, 130, 41, 271))
        palette14 = QPalette()
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush30 = QBrush(QColor(255, 246, 237, 128))
        brush30.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush30)
#endif
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush31 = QBrush(QColor(255, 246, 237, 128))
        brush31.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush31)
#endif
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush32 = QBrush(QColor(255, 246, 237, 128))
        brush32.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette14.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush32)
#endif
        self.line_5.setPalette(palette14)
        self.line_5.setAutoFillBackground(False)
        self.line_5.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_8 = QFrame(window)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(516, 130, 21, 271))
        palette15 = QPalette()
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush33 = QBrush(QColor(255, 246, 237, 128))
        brush33.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush33)
#endif
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush34 = QBrush(QColor(255, 246, 237, 128))
        brush34.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush34)
#endif
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush35 = QBrush(QColor(255, 246, 237, 128))
        brush35.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette15.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush35)
#endif
        self.line_8.setPalette(palette15)
        self.line_8.setAutoFillBackground(False)
        self.line_8.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_9 = QFrame(window)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(620, 130, 31, 271))
        palette16 = QPalette()
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush36 = QBrush(QColor(255, 246, 237, 128))
        brush36.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush36)
#endif
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush37 = QBrush(QColor(255, 246, 237, 128))
        brush37.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush37)
#endif
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush38 = QBrush(QColor(255, 246, 237, 128))
        brush38.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette16.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush38)
#endif
        self.line_9.setPalette(palette16)
        self.line_9.setAutoFillBackground(False)
        self.line_9.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_10 = QFrame(window)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(710, 130, 21, 271))
        palette17 = QPalette()
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush39 = QBrush(QColor(255, 246, 237, 128))
        brush39.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush39)
#endif
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush40 = QBrush(QColor(255, 246, 237, 128))
        brush40.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush40)
#endif
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush41 = QBrush(QColor(255, 246, 237, 128))
        brush41.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette17.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush41)
#endif
        self.line_10.setPalette(palette17)
        self.line_10.setAutoFillBackground(False)
        self.line_10.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_11 = QFrame(window)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(0, 390, 721, 21))
        palette18 = QPalette()
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush42 = QBrush(QColor(255, 246, 237, 128))
        brush42.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush42)
#endif
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush43 = QBrush(QColor(255, 246, 237, 128))
        brush43.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush43)
#endif
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush44 = QBrush(QColor(255, 246, 237, 128))
        brush44.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette18.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush44)
#endif
        self.line_11.setPalette(palette18)
        self.line_11.setAutoFillBackground(False)
        self.line_11.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_7 = QFrame(window)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(-10, 130, 20, 251))
        palette19 = QPalette()
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush45 = QBrush(QColor(255, 246, 237, 128))
        brush45.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush45)
#endif
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush46 = QBrush(QColor(255, 246, 237, 128))
        brush46.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush46)
#endif
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush47 = QBrush(QColor(255, 246, 237, 128))
        brush47.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette19.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush47)
#endif
        self.line_7.setPalette(palette19)
        self.line_7.setAutoFillBackground(False)
        self.line_7.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_12 = QFrame(window)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setGeometry(QRect(0, 150, 721, 16))
        palette20 = QPalette()
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush48 = QBrush(QColor(255, 246, 237, 128))
        brush48.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush48)
#endif
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush49 = QBrush(QColor(255, 246, 237, 128))
        brush49.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush49)
#endif
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush50 = QBrush(QColor(255, 246, 237, 128))
        brush50.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette20.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush50)
#endif
        self.line_12.setPalette(palette20)
        self.line_12.setAutoFillBackground(False)
        self.line_12.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_14 = QLabel(window)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(300, 140, 41, 16))
        self.label_14.setFont(font2)
        self.label_15 = QLabel(window)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(470, 140, 41, 16))
        self.label_15.setFont(font2)
        self.label_16 = QLabel(window)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(660, 140, 41, 16))
        self.label_16.setFont(font2)
        self.Report_no_box = QLineEdit(window)
        self.Report_no_box.setObjectName(u"Report_no_box")
        self.Report_no_box.setGeometry(QRect(660, 400, 51, 21))
        self.Report_no_box.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")
        self.Report_no_label = QLabel(window)
        self.Report_no_label.setObjectName(u"Report_no_label")
        self.Report_no_label.setGeometry(QRect(590, 400, 71, 20))
        font4 = QFont()
        font4.setFamilies([u"Arial Black"])
        font4.setBold(True)
        self.Report_no_label.setFont(font4)
        self.Report_no_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.gridLayoutWidget_2 = QWidget(window)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 30, 601, 92))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.reptPrintDateLabel = QLabel(self.gridLayoutWidget_2)
        self.reptPrintDateLabel.setObjectName(u"reptPrintDateLabel")
        self.reptPrintDateLabel.setFont(font4)
        self.reptPrintDateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.reptPrintDateLabel, 3, 6, 1, 1)

        self.SampleType = QLabel(self.gridLayoutWidget_2)
        self.SampleType.setObjectName(u"SampleType")
        self.SampleType.setFont(font4)
        self.SampleType.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.SampleType, 3, 3, 1, 1)

        self.PID_label = QLabel(self.gridLayoutWidget_2)
        self.PID_label.setObjectName(u"PID_label")
        self.PID_label.setFont(font4)
        self.PID_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.PID_label, 1, 4, 1, 1)

        self.gender_combo_box = QComboBox(self.gridLayoutWidget_2)
        self.gender_combo_box.addItem("")
        self.gender_combo_box.addItem("")
        self.gender_combo_box.addItem("")
        self.gender_combo_box.setObjectName(u"gender_combo_box")

        self.gridLayout_2.addWidget(self.gender_combo_box, 2, 4, 1, 1)

        self.regDateLabel = QLabel(self.gridLayoutWidget_2)
        self.regDateLabel.setObjectName(u"regDateLabel")
        self.regDateLabel.setFont(font4)
        self.regDateLabel.setLayoutDirection(Qt.LeftToRight)
        self.regDateLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.regDateLabel, 1, 6, 1, 1)

        self.smplTestD_Box = QDateTimeEdit(self.gridLayoutWidget_2)
        self.smplTestD_Box.setObjectName(u"smplTestD_Box")
        self.smplTestD_Box.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.smplTestD_Box, 2, 7, 1, 1)

        self.smplTestDate = QLabel(self.gridLayoutWidget_2)
        self.smplTestDate.setObjectName(u"smplTestDate")
        self.smplTestDate.setFont(font4)
        self.smplTestDate.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.smplTestDate, 2, 6, 1, 1)

        self.PID_box = QLineEdit(self.gridLayoutWidget_2)
        self.PID_box.setObjectName(u"PID_box")
        self.PID_box.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.PID_box, 1, 5, 1, 1)

        self.Name_label = QLabel(self.gridLayoutWidget_2)
        self.Name_label.setObjectName(u"Name_label")
        self.Name_label.setFont(font4)
        self.Name_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.Name_label, 1, 0, 1, 1)

        self.regDateBox = QDateEdit(self.gridLayoutWidget_2)
        self.regDateBox.setObjectName(u"regDateBox")
        self.regDateBox.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.regDateBox, 1, 7, 1, 1)

        self.Age_box = QLineEdit(self.gridLayoutWidget_2)
        self.Age_box.setObjectName(u"Age_box")
        self.Age_box.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.Age_box, 2, 1, 1, 1)

        self.sampleTypeBox = QLineEdit(self.gridLayoutWidget_2)
        self.sampleTypeBox.setObjectName(u"sampleTypeBox")
        self.sampleTypeBox.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.sampleTypeBox, 3, 4, 1, 2)

        self.Age_label = QLabel(self.gridLayoutWidget_2)
        self.Age_label.setObjectName(u"Age_label")
        self.Age_label.setFont(font4)
        self.Age_label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.Age_label, 2, 0, 1, 1)

        self.Name_box = QLineEdit(self.gridLayoutWidget_2)
        self.Name_box.setObjectName(u"Name_box")
        self.Name_box.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.Name_box, 1, 1, 1, 3)

        self.ref_by_box = QComboBox(self.gridLayoutWidget_2)
        self.ref_by_box.setObjectName(u"ref_by_box")

        self.gridLayout_2.addWidget(self.ref_by_box, 3, 1, 1, 1)

        self.reptPrintD_box = QDateTimeEdit(self.gridLayoutWidget_2)
        self.reptPrintD_box.setObjectName(u"reptPrintD_box")
        self.reptPrintD_box.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.reptPrintD_box, 3, 7, 1, 1)

        self.refBY = QLabel(self.gridLayoutWidget_2)
        self.refBY.setObjectName(u"refBY")
        self.refBY.setFont(font4)

        self.gridLayout_2.addWidget(self.refBY, 3, 0, 1, 1)

        self.Gender_label = QLabel(self.gridLayoutWidget_2)
        self.Gender_label.setObjectName(u"Gender_label")
        self.Gender_label.setFont(font4)
        self.Gender_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.Gender_label, 2, 3, 1, 1)

        self.cmntBox = QPlainTextEdit(window)
        self.cmntBox.setObjectName(u"cmntBox")
        self.cmntBox.setGeometry(QRect(10, 420, 561, 61))
        self.cmntBox.setStyleSheet(u"background-color: #FAF9F6;\n"
"border: 1px solid black;\n"
"height: 1.6em;\n"
"border-radius: 5px;")
        self.cmntLabel = QLabel(window)
        self.cmntLabel.setObjectName(u"cmntLabel")
        self.cmntLabel.setGeometry(QRect(10, 400, 81, 20))
        self.cmntLabel.setFont(font4)
        self.cmntLabel.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.line_6 = QFrame(window)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(0, 120, 721, 20))
        palette21 = QPalette()
        palette21.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette21.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette21.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush51 = QBrush(QColor(255, 246, 237, 128))
        brush51.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush51)
#endif
        palette21.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette21.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette21.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush52 = QBrush(QColor(255, 246, 237, 128))
        brush52.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush52)
#endif
        palette21.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette21.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette21.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush53 = QBrush(QColor(255, 246, 237, 128))
        brush53.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette21.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush53)
#endif
        self.line_6.setPalette(palette21)
        self.line_6.setAutoFillBackground(False)
        self.line_6.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.Machine_conn_check = QCheckBox(window)
        self.Machine_conn_check.setObjectName(u"Machine_conn_check")
        self.Machine_conn_check.setGeometry(QRect(600, 440, 70, 17))
        self.Machine_conn_check.setChecked(False)
        self.line_13 = QFrame(window)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setGeometry(QRect(570, 400, 21, 101))
        palette22 = QPalette()
        palette22.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette22.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette22.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush54 = QBrush(QColor(255, 246, 237, 128))
        brush54.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush54)
#endif
        palette22.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette22.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette22.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush55 = QBrush(QColor(255, 246, 237, 128))
        brush55.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush55)
#endif
        palette22.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette22.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette22.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush56 = QBrush(QColor(255, 246, 237, 128))
        brush56.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette22.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush56)
#endif
        self.line_13.setPalette(palette22)
        self.line_13.setAutoFillBackground(False)
        self.line_13.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_14 = QFrame(window)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(0, 490, 721, 21))
        palette23 = QPalette()
        palette23.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette23.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette23.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush57 = QBrush(QColor(255, 246, 237, 128))
        brush57.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush57)
#endif
        palette23.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette23.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette23.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush58 = QBrush(QColor(255, 246, 237, 128))
        brush58.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush58)
#endif
        palette23.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette23.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette23.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush59 = QBrush(QColor(255, 246, 237, 128))
        brush59.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette23.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush59)
#endif
        self.line_14.setPalette(palette23)
        self.line_14.setAutoFillBackground(False)
        self.line_14.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_15 = QFrame(window)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(710, 400, 21, 101))
        palette24 = QPalette()
        palette24.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush17)
        palette24.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush17)
        palette24.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush17)
        brush60 = QBrush(QColor(255, 246, 237, 128))
        brush60.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush60)
#endif
        palette24.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush17)
        palette24.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush17)
        palette24.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush17)
        brush61 = QBrush(QColor(255, 246, 237, 128))
        brush61.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush61)
#endif
        palette24.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush17)
        palette24.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush17)
        palette24.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        brush62 = QBrush(QColor(255, 246, 237, 128))
        brush62.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette24.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush62)
#endif
        self.line_15.setPalette(palette24)
        self.line_15.setAutoFillBackground(False)
        self.line_15.setStyleSheet(u"color: rgb(255, 246, 237);")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)
        self.progressBar = QProgressBar(window)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(600, 460, 111, 23))
        self.progressBar.setValue(24)
        QWidget.setTabOrder(self.Age_box, self.RBC_val)
        QWidget.setTabOrder(self.RBC_val, self.HGB_val)
        QWidget.setTabOrder(self.HGB_val, self.HCT_val)
        QWidget.setTabOrder(self.HCT_val, self.MCV_val)
        QWidget.setTabOrder(self.MCV_val, self.MCH_val)
        QWidget.setTabOrder(self.MCH_val, self.MCHC_val)
        QWidget.setTabOrder(self.MCHC_val, self.RDW_CV_val)
        QWidget.setTabOrder(self.RDW_CV_val, self.RDW_SD_val)
        QWidget.setTabOrder(self.RDW_SD_val, self.WBC_val)
        QWidget.setTabOrder(self.WBC_val, self.NEU_per_val)
        QWidget.setTabOrder(self.NEU_per_val, self.LYM_per_val)
        QWidget.setTabOrder(self.LYM_per_val, self.MON_per_val)
        QWidget.setTabOrder(self.MON_per_val, self.EOS_per_val)
        QWidget.setTabOrder(self.EOS_per_val, self.BAS_per_val)
        QWidget.setTabOrder(self.BAS_per_val, self.WBC_ref)
        QWidget.setTabOrder(self.WBC_ref, self.NEU_per_ref)
        QWidget.setTabOrder(self.NEU_per_ref, self.LYM_per_ref)
        QWidget.setTabOrder(self.LYM_per_ref, self.MON_per_ref)
        QWidget.setTabOrder(self.MON_per_ref, self.EOS_per_ref)
        QWidget.setTabOrder(self.EOS_per_ref, self.BAS_per_ref)
        QWidget.setTabOrder(self.BAS_per_ref, self.NEU_hash_val)
        QWidget.setTabOrder(self.NEU_hash_val, self.LYM_hash_val)
        QWidget.setTabOrder(self.LYM_hash_val, self.MON_hash_val)
        QWidget.setTabOrder(self.MON_hash_val, self.EOS_hash_val)
        QWidget.setTabOrder(self.EOS_hash_val, self.BAS_hash_val)
        QWidget.setTabOrder(self.BAS_hash_val, self.NEU_hash_ref)
        QWidget.setTabOrder(self.NEU_hash_ref, self.LYM_hash_ref)
        QWidget.setTabOrder(self.LYM_hash_ref, self.MON_hash_ref)
        QWidget.setTabOrder(self.MON_hash_ref, self.EOS_hash_ref)
        QWidget.setTabOrder(self.EOS_hash_ref, self.BAS_hash_ref)
        QWidget.setTabOrder(self.BAS_hash_ref, self.PLT_val)
        QWidget.setTabOrder(self.PLT_val, self.MPV_val)
        QWidget.setTabOrder(self.MPV_val, self.PDW_SD_val)
        QWidget.setTabOrder(self.PDW_SD_val, self.PDW_CV_val)
        QWidget.setTabOrder(self.PDW_CV_val, self.PCT_val)
        QWidget.setTabOrder(self.PCT_val, self.P_LCR_val)
        QWidget.setTabOrder(self.P_LCR_val, self.P_LCC_val)
        QWidget.setTabOrder(self.P_LCC_val, self.PLT_ref)
        QWidget.setTabOrder(self.PLT_ref, self.MPV_ref)
        QWidget.setTabOrder(self.MPV_ref, self.PDW_SD_ref)
        QWidget.setTabOrder(self.PDW_SD_ref, self.PDW_CV_ref)
        QWidget.setTabOrder(self.PDW_CV_ref, self.PCT_ref)
        QWidget.setTabOrder(self.PCT_ref, self.P_LCR_ref)
        QWidget.setTabOrder(self.P_LCR_ref, self.P_LCC_ref)
        QWidget.setTabOrder(self.P_LCC_ref, self.save_btn)
        QWidget.setTabOrder(self.save_btn, self.cancel_btn)
        QWidget.setTabOrder(self.cancel_btn, self.prev_btn)
        QWidget.setTabOrder(self.prev_btn, self.next_btn)
        QWidget.setTabOrder(self.next_btn, self.edit_btn)
        QWidget.setTabOrder(self.edit_btn, self.pdf_btn)
        QWidget.setTabOrder(self.pdf_btn, self.excel_btn)
        QWidget.setTabOrder(self.excel_btn, self.print_btn)
        QWidget.setTabOrder(self.print_btn, self.config_btn)

        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"Patient details (CBC)", None))
        self.prev_btn.setText(QCoreApplication.translate("window", u"PREV", None))
        self.print_btn.setText(QCoreApplication.translate("window", u"PRINT", None))
        self.edit_btn.setText(QCoreApplication.translate("window", u"EDIT", None))
        self.excel_btn.setText(QCoreApplication.translate("window", u"EXCEL", None))
        self.save_btn.setText(QCoreApplication.translate("window", u"SAVE", None))
        self.pdf_btn.setText(QCoreApplication.translate("window", u"PDF", None))
        self.next_btn.setText(QCoreApplication.translate("window", u"NEXT", None))
        self.config_btn.setText(QCoreApplication.translate("window", u"CONFIG.", None))
        self.cancel_btn.setText(QCoreApplication.translate("window", u"CANCEL", None))
        self.rBCLabel.setText(QCoreApplication.translate("window", u"RBC", None))
        self.hGBLabel.setText(QCoreApplication.translate("window", u"HGB", None))
        self.hCTLabel.setText(QCoreApplication.translate("window", u"HCT", None))
        self.mCVLabel.setText(QCoreApplication.translate("window", u"MCV", None))
        self.mCHLabel.setText(QCoreApplication.translate("window", u"MCH", None))
        self.mCHCLabel.setText(QCoreApplication.translate("window", u"MCHC", None))
        self.rDW_CVLabel.setText(QCoreApplication.translate("window", u"RDW-CV", None))
        self.rDW_SDLabel.setText(QCoreApplication.translate("window", u"RDW-SD", None))
        self.RBC_val.setText("")
        self.nEULabel.setText(QCoreApplication.translate("window", u"NEU%", None))
        self.lYMLabel.setText(QCoreApplication.translate("window", u"LYM%", None))
        self.mONLabel.setText(QCoreApplication.translate("window", u"MON%", None))
        self.eOSLabel.setText(QCoreApplication.translate("window", u"EOS%", None))
        self.bASLabel.setText(QCoreApplication.translate("window", u"BAS%", None))
        self.wBCLabel.setText(QCoreApplication.translate("window", u"WBC", None))
        self.nEULabel_2.setText(QCoreApplication.translate("window", u"NEU#", None))
        self.lYMLabel_2.setText(QCoreApplication.translate("window", u"LYM#", None))
        self.mONLabel_2.setText(QCoreApplication.translate("window", u"MON#", None))
        self.eOSLabel_2.setText(QCoreApplication.translate("window", u"EOS#", None))
        self.bASLabel_2.setText(QCoreApplication.translate("window", u"BAS#", None))
        self.pLTLabel.setText(QCoreApplication.translate("window", u"PLT", None))
        self.mPVLabel.setText(QCoreApplication.translate("window", u"MPV", None))
        self.pDWSDLabel.setText(QCoreApplication.translate("window", u"PDW-SD", None))
        self.pDWCVLabel.setText(QCoreApplication.translate("window", u"PDW-CV", None))
        self.pCTLabel.setText(QCoreApplication.translate("window", u"PCT", None))
        self.pLCRLabel.setText(QCoreApplication.translate("window", u"P-LCR", None))
        self.pLCCLabel.setText(QCoreApplication.translate("window", u"P-LCC", None))
        self.label.setText(QCoreApplication.translate("window", u"units", None))
        self.label_5.setText(QCoreApplication.translate("window", u"VALUES", None))
        self.label_6.setText(QCoreApplication.translate("window", u"RESULT", None))
        self.label_7.setText(QCoreApplication.translate("window", u"RESULT", None))
        self.label_8.setText(QCoreApplication.translate("window", u"VALUES", None))
        self.label_9.setText(QCoreApplication.translate("window", u"VALUES", None))
        self.label_10.setText(QCoreApplication.translate("window", u"VALUES", None))
        self.label_11.setText(QCoreApplication.translate("window", u"RESULT", None))
        self.label_12.setText(QCoreApplication.translate("window", u"RESULT", None))
        self.label_14.setText(QCoreApplication.translate("window", u"units", None))
        self.label_15.setText(QCoreApplication.translate("window", u"units", None))
        self.label_16.setText(QCoreApplication.translate("window", u"units", None))
        self.Report_no_label.setText(QCoreApplication.translate("window", u"Report no.", None))
        self.reptPrintDateLabel.setText(QCoreApplication.translate("window", u"Rept. Print D/T", None))
        self.SampleType.setText(QCoreApplication.translate("window", u"Sample TYPE", None))
        self.PID_label.setText(QCoreApplication.translate("window", u"PID", None))
        self.gender_combo_box.setItemText(0, QCoreApplication.translate("window", u"Male", None))
        self.gender_combo_box.setItemText(1, QCoreApplication.translate("window", u"Female", None))
        self.gender_combo_box.setItemText(2, QCoreApplication.translate("window", u"Others", None))

        self.regDateLabel.setText(QCoreApplication.translate("window", u"Reg date", None))
        self.smplTestDate.setText(QCoreApplication.translate("window", u"Sample Tested D/T", None))
        self.Name_label.setText(QCoreApplication.translate("window", u"Name", None))
        self.Age_box.setText(QCoreApplication.translate("window", u"aGE", None))
        self.Age_label.setText(QCoreApplication.translate("window", u"Age", None))
        self.Name_box.setText(QCoreApplication.translate("window", u"nAME", None))
        self.refBY.setText(QCoreApplication.translate("window", u"Ref. By ", None))
        self.Gender_label.setText(QCoreApplication.translate("window", u"Gender", None))
        self.cmntLabel.setText(QCoreApplication.translate("window", u"Comments:", None))
        self.Machine_conn_check.setText(QCoreApplication.translate("window", u"Machine", None))
    # retranslateUi

