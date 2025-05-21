import os
import json

def read_ip_list(filepath):
    """IP listesini dosyadan okuyup döner."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} bulunamadı.")
    with open(filepath, "r") as f:
        return [line.strip() for line in f if line.strip()]

def write_to_file(filepath, ip):
    """Belirtilen dosyaya IP'yi satır olarak yazar."""
    with open(filepath, "a") as f:
        f.write(f"{ip}\n")

def save_response(ip, data, directory):
    """IP için alınan JSON yanıtını dosyaya kaydeder."""
    if not os.path.exists(directory):
        os.makedirs(directory)
    filepath = os.path.join(directory, f"{ip}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
