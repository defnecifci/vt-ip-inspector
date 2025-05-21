# 🔍 VT IP Checker

VirusTotal Public API kullanarak IP adreslerinin analizini yapan, zararlı/süpheli IP'leri tespit eden Python uygulaması.

---

## 🚀 Özellikler

- `ips.txt` içinden IP adreslerini okur.
- Her IP için VirusTotal üzerinden analiz sorgusu yapar.
- Zararlı veya şüpheli bulunan IP'leri `malicious_ips.txt` dosyasına ekler.
- Bulunamayan IP'leri `not_found_ips.txt` içine yazar.
- Tüm yanıtları `responses/` klasörüne JSON formatında kaydeder.
- Modüler ve profesyonel Python yapısına sahiptir.

---

## 📁 Klasör Yapısı

```
vt_ip_checker/
├── data/
│   ├── ips.txt
│   ├── malicious_ips.txt
│   ├── not_found_ips.txt
├── responses/
├── src/
│   ├── run.py
│   ├── config.py
│   ├── vt_api.py
│   ├── file_utils.py
│   ├── analyzer.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Kurulum

```bash
# 1. Projeyi klonla
git clone <repo-url>
cd vt_ip_checker

# 2. Ortamı hazırla
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Gereksinimleri yükle
pip install -r requirements.txt

# 4. API anahtarını tanımla
touch .env
echo "VT_API_KEY=senin_virus_total_api_anahtarin" > .env

# 5. IP listeni oluştur
nano data/ips.txt

# 6. Çalıştır
python src/run.py
```

---

## 🎯 Örnek Değerlendirme Kriterleri:

| IP Adresi       | VT Analiz Sonucu                | Sınıflandırma        |
| --------------- | ------------------------------- | -------------------- |
| 104.219.13.197  | `malicious: 0`, `suspicious: 0` | Clean (Not Listed)   |
| 34.74.242.228   | `malicious: 5`, `suspicious: 3` | Malicious/Suspicious |
| 196.251.83.136  | `malicious: 12`, `suspicious: 1`| Malicious/Suspicious |
| 185.93.89.118   | `malicious: 16`, `suspicious: 2`| Malicious/Suspicious |
| 167.94.146.21   | `malicious: 1`, `suspicious: 1` | Malicious/Suspicious |
| 171.123.173.202 | `malicious: 4`, `suspicious: 0` | Malicious/Suspicious |
| 192.168.1.256   | Kayıt bulunamadı                | Not Found            |

---

## 📦 Gereksinimler

- Python 3.8+
- VirusTotal Public API key
- İnternet bağlantısı

---

## 📜 Lisans

MIT
