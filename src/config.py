import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

# Ortam değişkeninden API anahtarını çek
API_KEY = os.getenv("VT_API_KEY")

if not API_KEY:
    raise ValueError("API anahtarı .env dosyasından yüklenemedi. Lütfen VT_API_KEY tanımlı mı kontrol et.")
