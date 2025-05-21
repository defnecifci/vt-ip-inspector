import requests
from config import API_KEY

VT_BASE_URL = "https://www.virustotal.com/api/v3/ip_addresses/"

def analyze_ip(ip):
    """IP adresini VirusTotal API üzerinden analiz eder."""
    url = VT_BASE_URL + ip
    headers = {
        "x-apikey": API_KEY,
        "accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None  # Not found
        else:
            print(f"[!] {ip} için beklenmeyen yanıt: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"[!] {ip} için istek hatası: {e}")
        return None
