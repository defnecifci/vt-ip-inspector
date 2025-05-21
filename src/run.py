from file_utils import read_ip_list, write_to_file, save_response
from vt_api import analyze_ip
from analyzer import is_malicious_or_suspicious
import time

# Ayarlar
INPUT_FILE = "data/ips.txt"
MALICIOUS_FILE = "data/malicious_ips.txt"
NOT_FOUND_FILE = "data/not_found_ips.txt"
RESPONSES_DIR = "responses"
REQUEST_DELAY = 15  

def main():
    print("[*] IP listesi okunuyor...")
    ip_list = read_ip_list(INPUT_FILE)

    for ip in ip_list:
        print(f"[>] İşleniyor: {ip}")
        data = analyze_ip(ip)
        time.sleep(REQUEST_DELAY)

        if data is None:
            print(f"[-] Yanıt alınamadı: {ip}")
            write_to_file(NOT_FOUND_FILE, ip)
            continue

        save_response(ip, data, RESPONSES_DIR)

        analysis_stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        if is_malicious_or_suspicious(analysis_stats):
            print(f"[!] Zararlı/Şüpheli bulundu: {ip}")
            write_to_file(MALICIOUS_FILE, ip)
        else:
            print(f"[+] Temiz: {ip}")

    print("\n[✓] İşlem tamamlandı.")

if __name__ == "__main__":
    main()
