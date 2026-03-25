# 🧪 CBC HL7 Analyzer

A desktop application that processes raw HL7 data from CBC (Complete Blood Count) machines, converts it into structured format, and generates printable reports.

---

## 🚀 Features

- Parses raw HL7 machine output into structured patient data  
- Displays data through GUI (PySide6)  
- Generates professional reports (PDF + print support)  
- Stores patient records using SQLite3  
- Supports Excel export using openpyxl  

---

## 🛠️ Tech Stack

- Python  
- PySide6 (GUI)  
- SQLite3 (Database)  
- openpyxl (Excel export)  
- pywin32 (Windows integration for printing)  

---

## ⚙️ How It Works

1. Takes raw HL7 data from CBC machines  
2. Parses and extracts required parameters  
3. Displays structured data in GUI  
4. Generates formatted reports  
5. Stores records in local database  

---

## 📦 Installation

```bash
git clone https://github.com/simarCoder/cbc-hl7-analyzer
cd cbc-hl7-analyzer
pip install -r requirements.txt
python main.py
```
---

```md
## 📸 Screenshots

![Main UI](screenshots/main.png)
![Parsed Data](screenshots/data.png)
![Report](screenshots/report.png)

---

## 🎯 Purpose

This project simulates a real-world medical data processing system used in labs to automate report generation and data storage.

---

## ⚠️ Note

This is a local system designed for offline usage and does not include cloud integration.

---

## 🏢 Context

This project was developed as part of my own startup work to handle CBC machine data processing and report generation.

The version shared here is a cleaned and simplified version for demonstration and portfolio purposes.

---

## 👨‍💻 Author

**Simar**
GitHub: https://github.com/simarCoder