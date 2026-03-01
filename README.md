# 🛡️ Multi-Agent AI Security Log Analyzer

An AI-powered cybersecurity tool that automatically analyzes system logs, looks up real CVEs from the NIST National Vulnerability Database, maps attacks to the MITRE ATT&CK framework, and generates a timestamped professional incident report — all completely free.

---

## 🧠 How It Works

```
sample_logs.txt
      ↓
Agent 1: Log Analyzer       → Identifies attack type, services, IPs, and CVE keywords
      ↓
Agent 2: CVE Lookup Agent   → Searches NVD API for real CVEs matching the attack
      ↓
Agent 3: MITRE ATT&CK Agent → Maps attack behavior to real MITRE technique IDs
      ↓
Agent 4: Report Agent       → Combines everything into a timestamped incident report
```

Each agent is a specialist powered by **LLaMA 3.3 70B via Groq**. They run in sequence through `main.py`, passing their findings to the next agent — just like a real SOC team workflow.

---

## ✨ Features

- 🤖 **4-agent AI pipeline** — each agent has a dedicated role and system prompt
- 🔍 **Real CVE lookups** — queries the free NIST NVD API (no key needed) for live vulnerability data
- 🗺️ **MITRE ATT&CK mapping** — identifies tactics and techniques (e.g. T1110.001 - Password Guessing)
- 📝 **Auto-generated incident reports** — saved as timestamped `.txt` files with 8 structured sections
- 💰 **100% free** — Groq free tier + free public security APIs, no credit card required

---

## 📁 Project Structure

```
log-analyzer/
├── main.py                        # Orchestrator — runs all 4 agents in sequence
├── agents/
│   ├── log_agent.py               # Agent 1: Parses logs, extracts attack details
│   ├── cve_agent.py               # Agent 2: AI keyword extraction + NVD CVE search
│   ├── mitre_agent.py             # Agent 3: Maps findings to MITRE ATT&CK framework
│   └── report_agent.py            # Agent 4: Generates and saves final incident report
├── sample_logs.txt                # Input: paste your logs here
├── security_report_TIMESTAMP.txt  # Output: auto-generated after each run
├── .env                           # Your Groq API key (never share this)
├── .gitignore                     # Keeps .env out of GitHub
└── requirements.txt               # groq, python-dotenv, requests
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/log-analyzer.git
cd log-analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` contains:
```
groq
python-dotenv
requests
```

### 3. Get Your Free Groq API Key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for free — no credit card needed
3. Navigate to **API Keys** and generate a new key

### 4. Set Up Your `.env` File

Create a `.env` file in the root of the project:

```
GROQ_API_KEY=your_actual_key_here
```

> ⚠️ **Never share your `.env` file or push it to GitHub.** The `.gitignore` already excludes it.

### 5. Add Your Logs

Paste your server or system logs into `sample_logs.txt`. Example:

```
2024-01-15 03:22:01 Failed login attempt for user 'admin' from IP 192.168.1.105
2024-01-15 03:22:05 Failed login attempt for user 'admin' from IP 192.168.1.105
2024-01-15 03:22:09 Failed login attempt for user 'admin' from IP 192.168.1.105
2024-01-15 03:22:13 Failed login attempt for user 'admin' from IP 192.168.1.105
2024-01-15 03:22:17 Successful login for user 'admin' from IP 192.168.1.105
2024-01-15 03:25:44 User 'admin' accessed /etc/passwd
2024-01-15 03:26:10 User 'admin' downloaded 500MB of data
2024-01-15 08:00:01 Scheduled backup completed successfully
2024-01-15 08:15:22 Normal user 'john' logged in from IP 10.0.0.5
```

### 6. Run the Framework

```bash
python main.py
```

---

## 📊 Example Output

```
==================================================
🤖 MULTI-AGENT SECURITY ANALYSIS STARTING
==================================================

[Agent 1] 📋 Analyzing logs...
✅ Log analysis complete

[Agent 2] 🔍 Searching CVE database...
  🔍 Searching CVEs for: OpenSSH
  🔍 Searching CVEs for: Linux
  🔍 Searching CVEs for: FileZilla
✅ CVE lookup complete

[Agent 3] 🗺️  Mapping to MITRE ATT&CK...
✅ MITRE mapping complete

[Agent 4] 📝 Generating final report...
✅ Report saved to: security_report_20260222_230258.txt

==================================================
📊 FINAL REPORT PREVIEW
==================================================
```

---

## 📄 Report Structure

Every generated report contains these 8 sections:

1. **Executive Summary** — 2-3 sentence non-technical overview
2. **Incident Overview** — what happened and how
3. **Attack Timeline** — sequence of events reconstructed from the logs
4. **CVE Vulnerabilities Identified** — real CVEs from NVD with CVSS scores
5. **MITRE ATT&CK Mapping** — tactics and technique IDs with direct links
6. **Risk Severity** — Critical / High / Medium / Low with justification
7. **Immediate Actions Required** — what to do right now
8. **Long-Term Recommendations** — how to prevent recurrence

### Real Report Sample (from actual run on the sample logs)

```
SECURITY INCIDENT REPORT
Generated: 2026-02-22 23:02:58
Keywords Analyzed: OpenSSH, Linux, FileZilla

EXECUTIVE SUMMARY
A brute-force attack was detected from IP 192.168.1.105, resulting in
unauthorized admin access, sensitive file exposure (/etc/passwd), and
potential exfiltration of 500MB of data. Immediate action is required.

RISK SEVERITY: HIGH
CVEs Found   : CVE-1999-0661, CVE-2000-0525 (OpenSSH), CVE-2000-0508 (Linux)
MITRE Mapping: T1110.001 (Password Guessing), T1068 (Privilege Escalation),
               T1041 (Exfiltration Over C2 Channel), T1078 (Valid Accounts)
```

---

## 🧩 Agent Breakdown

| Agent | File | What It Does | API Used |
|-------|------|-------------|----------|
| Log Analyzer | `log_agent.py` | Identifies attack type, services, IPs, CVE keywords | Groq LLaMA 3.3 70B |
| CVE Agent | `cve_agent.py` | AI extracts keywords → searches NVD for real CVEs | Groq + NVD API |
| MITRE Agent | `mitre_agent.py` | Maps findings to ATT&CK tactics and technique IDs | Groq LLaMA 3.3 70B |
| Report Agent | `report_agent.py` | Compiles all results, saves timestamped `.txt` report | Groq LLaMA 3.3 70B |

---

## 🛠️ Tech Stack

| Tool | Purpose | Cost |
|------|---------|------|
| [Groq](https://console.groq.com) | AI inference — LLaMA 3.3 70B | Free tier |
| [NIST NVD API](https://nvd.nist.gov/developers/vulnerabilities) | Real CVE vulnerability database | Free, no key needed |
| [MITRE ATT&CK](https://attack.mitre.org) | Cybersecurity attack framework reference | Free |
| `python-dotenv` | Secure API key management via `.env` | Free |
| `requests` | HTTP calls to NVD API | Free |

---

## 🔒 Security Best Practices Used in This Project

- API key stored in `.env` and excluded from Git via `.gitignore` — never hardcoded in source
- External API calls wrapped in `try/except` to handle failures gracefully
- NVD results capped at 5 per keyword to respect free tier rate limits
- No sensitive log data is stored or transmitted beyond the local machine

---

## 📈 Ideas to Extend This Project

- [ ] Add a **Flask web UI** — paste logs in a browser instead of a text file
- [ ] **Email alerts** when report severity is Critical
- [ ] Support **Windows Event Log** and **JSON log formats**
- [ ] Add **Agent 5: Threat Intel** using the free VirusTotal API to check flagged IPs
- [ ] Export reports as **PDF** with proper formatting
- [ ] Schedule **auto-scanning** of a watched log folder using `cron`
- [ ] Post alerts to a **Slack channel** via webhook when threats are detected

---

## 📚 What You Learn Building This

- Multi-agent AI architecture and orchestration patterns
- Working with real cybersecurity APIs (NVD, MITRE ATT&CK)
- LLM prompt engineering with role-based system messages
- Secure environment variable management
- SOC (Security Operations Center) incident response workflows
- Log analysis and threat identification fundamentals

---

## ⚠️ Disclaimer

This tool is built for **educational purposes and personal learning**. It is not a replacement for professional security tooling or a qualified security analyst. Always verify AI-generated findings before acting on them in a production environment.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 👤 Author

Built by [Your Name]

> 💡 **Tip:** Add `security_report_*.txt` to your `.gitignore` so real incident data is never accidentally pushed to a public repository.
