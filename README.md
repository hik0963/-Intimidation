# Intimadation

A Python-based malware analysis and response tool powered by the VirusTotal API.

## 📘 Project Overview

**Intimadation** was created after encountering an attacker who quickly analyzed and broke down a highly advanced sample. This tool helps defenders do the same — extract detailed information about malware, generate a technical summary, and optionally use that data to respond to the sender.

## 🔍 Features

- Upload files to VirusTotal
- Retrieve analysis reports
- Extract:
  - SHA-256 hashes
  - AV detection names
  - Behavioral indicators
  - Obfuscation and encryption signs
- Generate a concise intelligence summary

## 📦 Requirements

- Python 3.8+
- VirusTotal API key
- Internet access (for VirusTotal integration)

Install dependencies:

```bash
pip install requests
