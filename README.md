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

## 📦 Gereksinimler

- Python 3.8+
- VirusTotal Public API key
- internet bağlantısı

---

## 📜 Lisans

MIT
