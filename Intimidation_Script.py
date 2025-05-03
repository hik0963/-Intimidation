import requests
import hashlib
import time

# Your VirusTotal API key
API_KEY = "YOUR_API_KEY"
HEADERS = {
    "x-apikey": API_KEY
}

VT_BASE_URL = "https://www.virustotal.com/api/v3"


def get_sha256(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def upload_file(file_path):
    url = f"{VT_BASE_URL}/files"
    with open(file_path, "rb") as f:
        files = {'file': f}
        response = requests.post(url, headers=HEADERS, files=files)
    if response.status_code == 200:
        return response.json()["data"]["id"]
    else:
        print(f"[!] Upload failed: {response.status_code}")
        return None


def get_report(file_id):
    url = f"{VT_BASE_URL}/analyses/{file_id}"
    while True:
        response = requests.get(url, headers=HEADERS)
        data = response.json()
        if data["data"]["attributes"]["status"] == "completed":
            return data
        print("[*] Waiting for analysis...")
        time.sleep(5)


def get_detailed_info(sha256):
    url = f"{VT_BASE_URL}/files/{sha256}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"[!] Could not retrieve detailed info: {response.status_code}")
        return None


def intimidate(file_path):
    print("[*] Uploading file to VirusTotal...")
    file_id = upload_file(file_path)
    if not file_id:
        return

    report = get_report(file_id)
    sha256 = report["meta"]["file_info"]["sha256"]
    print("[*] Retrieving detailed report...")
    details = get_detailed_info(sha256)
    
    malicious_count = details["data"]["attributes"]["last_analysis_stats"]["malicious"]
    total_engines = sum(details["data"]["attributes"]["last_analysis_stats"].values())
    av_hits = details["data"]["attributes"]["last_analysis_results"]
    
    detection_names = [av_hits[engine]["result"] for engine in av_hits if av_hits[engine]["result"]]
    unique_names = list(set(detection_names))[:5]  # Only show a few
    
    # Craft the intimidation message
    message = f"""
Your malware was fully dissected.

SHA-256: {sha256}
Detected by: {malicious_count}/{total_engines} AV engines
Sample detection names:
 - {chr(10).join(unique_names)}

We’ve identified:
 - C2 Servers: Under investigation
 - Obfuscation: Detected
 - Encryption: Likely AES/RSA (based on static signature)
 - Payload behavior: Suspicious activity patterns logged

You've been exposed. We’re logging your attack for further action.

- DefenderX
"""
    print(message)


# Replace with your file path
intimidate("sample_malware.exe")
