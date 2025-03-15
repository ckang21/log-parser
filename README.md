# 📝 Log Parser & Error Tracker

## 📌 Overview
This Python command-line tool **reads log files**, extracts `ERROR` messages, and saves them in **text (`errors.log`)** and **JSON (`errors.json`)** formats for easy debugging.  

## 🚀 Features
✅ **Filters Errors:** Only extracts `ERROR` messages  
✅ **Timestamps:** Extracts timestamps from logs (if available)  
✅ **Saves to File:** Errors are logged in both **text & JSON format**  
✅ **Command-Line Friendly:** Run it easily from the terminal  

---

## **🛠️ How to Use**

### **1️⃣ Install Dependencies**
Make sure you have Python installed, then install the required package:
```bash
pip install click
```
### **2️⃣ Run the Script**
```
python3 log_parser.py test.log
```

## Example
### `test.log`
```
[2025-03-11 10:00:00] INFO: System started
[2025-03-11 10:05:00] ERROR: Something went wrong!
[2025-03-11 10:10:00] WARNING: Low disk space
[2025-03-11 10:15:00] ERROR: Database connection failed
[2025-03-11 10:20:00] INFO: User logged in
```

### `errors.log` (Output)
```
2025-03-11 10:05:00 - [2025-03-11 10:05:00] ERROR: Something went wrong!
2025-03-11 10:15:00 - [2025-03-11 10:15:00] ERROR: Database connection failed
```

### `errors.json` (JSON Output)
```json
[
    {
        "timestamp": "2025-03-11 10:05:00",
        "message": "[2025-03-11 10:05:00] ERROR: Something went wrong!"
    },
    {
        "timestamp": "2025-03-11 10:15:00",
        "message": "[2025-03-11 10:15:00] ERROR: Database connection failed"
    }
]
```

Built by Christian Kang as a personal project