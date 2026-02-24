# 🌐 Network Monitoring Toolkit

A modular, multi-device network monitoring and automation toolkit built using Python.

This project simulates an enterprise-grade Network Operations Center (NOC) monitoring system capable of analyzing router interface health, calculating SLA-based scores, and generating a professional HTML dashboard.

---

## 🚀 Project Overview

The Network Monitoring Toolkit automates the process of:

- Connecting to multiple routers (real or simulated)
- Fetching interface status via CLI commands
- Parsing and analyzing interface health
- Calculating SLA-based health scores
- Classifying device status (HEALTHY / STABLE / CRITICAL)
- Generating a visual HTML monitoring dashboard
- Logging execution details

This tool demonstrates real-world network automation architecture used in enterprise environments.

---

## 🏗 Architecture

CLI (main.py)  
↓  
Device Manager (device_manager.py)  
↓  
Analyzer (analyzer.py)  
↓  
Health Engine (SLA Scoring)  
↓  
HTML Dashboard Generator  
↓  
Logs  

The project follows modular design principles to ensure scalability and maintainability.

---

## 🧰 Technologies Used

- Python 3
- Netmiko (SSH to network devices)
- PyYAML (Configuration management)
- argparse (CLI interface)
- HTML + CSS (Dashboard UI)
- Python logging module
- Random module (Simulation mode)

---

## 📂 Project Structure

```
Network_Monitoring_Toolkit/
│
├── main.py
├── device_manager.py
├── analyzer.py
├── report_generator.py
├── logger.py
├── config/
│     └── devices.yaml
├── reports/
│     └── dashboard.html
├── logs/
│     └── network.log
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```
git clone <your-repo-link>
cd Network_Monitoring_Toolkit
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🖥 Usage

### 🔹 Simulation Mode (No real router required)

```
python main.py --config config/devices.yaml --demo
```

This will:
- Generate simulated router output
- Analyze interface health
- Create HTML dashboard
- Generate logs

---

### 🔹 Real Router Mode (Requires SSH Access)

Update `config/devices.yaml`:

```
devices:
  - name: Router1
    device_type: cisco_ios
    host: 192.168.1.10
    username: admin
    password: admin123
```

Run:

```
python main.py --config config/devices.yaml
```

---

## 📊 Dashboard Output

The tool generates:

```
reports/dashboard.html
```

The dashboard includes:

- Device Name
- Total Interfaces
- Interfaces Down
- Health Score (%)
- Color-coded Status:
  - 🟢 HEALTHY
  - 🟡 STABLE
  - 🔴 CRITICAL

---

## 📈 SLA Health Calculation Logic

Health % = (Working Interfaces / Total Interfaces) × 100

Status Classification:

| Health Score | Status   |
|--------------|----------|
| 100%         | HEALTHY  |
| 70–99%       | STABLE   |
| <70%         | CRITICAL |

---

## 🧪 Features

- Multi-device monitoring
- YAML-based configuration
- Simulation mode for testing
- Real device SSH connectivity
- SLA-based health scoring
- Structured logging
- HTML dashboard reporting
- CLI-driven execution

---

## 🏢 Real-World Relevance

This project simulates enterprise monitoring systems used in:

- Network Operations Centers (NOC)
- Field Service Engineering teams
- Routing & Switching environments
- Telecom infrastructure monitoring
- SLA-based service validation systems

---

## 📌 Future Enhancements

- Email alerts for CRITICAL devices
- Chart.js graphical analytics
- Flask live web dashboard
- REST API integration
- Docker containerization
- Cloud deployment
- Database integration

---

## 👩‍💻 Author

Pedapati Lashya Saranya  
Aspiring Network & Automation Engineer  

---

## ⭐ Key Learning Outcomes

- Network CLI parsing
- Automation scripting
- SLA-based health modeling
- Multi-device architecture
- Modular system design
- Dashboard generation
- Enterprise logging practices