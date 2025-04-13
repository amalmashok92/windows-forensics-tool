# Windows Forensics Tool 🛡️

A Python-based tool designed for collecting important forensic artifacts from Windows systems.  
Built for cybersecurity professionals, incident responders, and forensic analysts.

---

## Features ✨

- Extract Live Windows Registry data
- Analyze Offline Registry Hive files (like `NTUSER.DAT`)
- Collect Windows Event Logs
- Extract Browser History (Chrome, Edge, Firefox)
- Modular & Extensible Design
- Python-based, Lightweight, Easy to Use

---

## Installation 🚀

Clone the repo:
```bash
git clone https://github.com/amalmashok92/windows-forensics-tool.git
cd windows-forensics-tool
Install dependencies:

bash
pip install -r requirements.txt

Usage Examples ⚙️
Extract Live Registry (RunMRU key)

bash
python -m forensics.main --registry

Extract Offline Registry Hive (NTUSER.DAT)

bash
C:\Users\<username>\NTUSER.DAT C:\Temp\NTUSER.DAT
python -m forensics.main --registry --hive-path "C:\Temp\NTUSER.DAT"
Extract Specific Registry Key

bash
python -m forensics.main --registry --hive-path "C:\Temp\NTUSER.DAT" --reg-key "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

Collect Windows Event Logs

bash
python -m forensics.main --events
Extract Browser History
bash


python -m forensics.main --browser
Project Structure 🗂️
arduino


windows-forensics-tool/
├── forensics/
│   ├── main.py
│   ├── registry_analysis.py
│   ├── event_logs.py
│   └── browser_artifacts.py
├── tests/
│   └── test_*.py
├── .github/workflows/
│   └── python-app.yml
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md

Running Tests 🧪

bash
pytest

Note on Offline Registry Files ⚠️
	NTUSER.DAT is usually locked.
	copy it first:

cmd
C:\Users\<username>\NTUSER.DAT C:\Temp\NTUSER.DAT
Contributing 🤝
Pull requests are welcome. Please raise issues or ideas!

License 📜
This project is licensed under the MIT License.