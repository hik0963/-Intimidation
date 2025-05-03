# 🛡️ Intimadation

**Intimadation** is a Python-based malware analysis tool that uploads a suspicious file to VirusTotal, retrieves deep insights, and presents the results in a readable, intimidation-ready format. Ideal for defenders, malware researchers, and enthusiasts who want to stay 20 steps ahead.

Inspired by a personal encounter where an attacker reversed a nation-state-grade Trojan within seconds — this tool gives you an edge to strike back with knowledge.

---

## 🔍 What It Does

- Uploads any file to VirusTotal for analysis
- Retrieves:
  - SHA-256 hash
  - Antivirus detection stats
  - Detection names
  - Behavioral traits (obfuscation, encryption, etc.)
- Prints a summary that can be added to your personal threat definitions or used to respond to attackers

---

## 🧰 Requirements

- Python 3.8+
- A free [VirusTotal](https://www.virustotal.com/) API key
- `requests` Python module

---


---

## 🔑 VirusTotal API Setup

1. Create an account at [https://www.virustotal.com](https://www.virustotal.com)
2. Go to your profile → API key
3. Copy the key

Open `intimadation.py` and find:

```python
API_KEY = "YOUR_API_KEY"


git clone https://github.com/hik0963/intimadation.git
cd intimadation

pip install requests

---

## ONLY 14 CHILL PEEOPLES

---

# Then find:
intimidate("sample_malware.exe")
Replace with your file path

