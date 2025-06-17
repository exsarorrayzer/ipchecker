---

# 🇺🇸 IP Information Lookup Tool 🔍


## 📌 Overview
A Python tool that fetches detailed information about any IP address using the ip-api.com service. Provides geolocation, ISP details, and security information with beautiful console output.

## 🌟 Features
- **Complete IP Analysis** - Country, city, ISP, and more
- **Security Checks** - Detect proxies/VPNs/Tor exits
- **Rich Visual Output** - Colorful console presentation
- **Fallback Support** - Works without Rich library
- **Easy Setup** - Automatic dependency installation

## 📦 Installation
```bash
# Clone the repository
git clone https://github.com/exsarorrayzer/ipchecker.git
cd ipchecker

# Run setup (auto-installs dependencies)
python setup.py
```

## 🚀 Usage
```bash
python main.py
```
Then either:
- Enter an IP address to lookup
- Press Enter to check your own IP

## 🛠️ Technical Details
### Dependencies
- `requests` - For API communication
- `rich` - For beautiful console output (optional)

### File Structure
```
ipchecker/
├── main.py       # Main application
├── setup.py           # Installation script
└── requirements.txt   # Dependency list
```

## ⚠️ Important Notes
- Free ip-api.com limits: 45 requests/minute
- Requires Python 3.6+
- Works on Windows/Linux/macOS
- For educational purposes only

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨💻 Author
**Rayzer** - [@exsarorrayzer](https://github.com/exsarorrayzer)

---

### 🔧 Troubleshooting
**Problem**: Rate limit errors  
**Solution**: Wait 1 minute between requests or use `--wait` parameter

**Problem**: Missing geolocation data  
**Solution**: Some IPs (especially cloud providers) have limited info

**Problem**: Rich not installing  
**Solution**: Tool works without it (basic output mode)

---

### 🌐 API Reference
This tool uses the free [ip-api.com](https://ip-api.com/docs) service. Consider their pro service for:
- Higher rate limits
- HTTPS support
- Commercial use

---

# 🇹🇷 IP Bilgisi Arama Aracı 🔍

## 📌 Genel Bakış
ip-api.com hizmetini kullanarak herhangi bir IP adresi hakkında ayrıntılı bilgi alan bir Python aracı. Güzel konsol çıktısı ile coğrafi konum, ISP ayrıntıları ve güvenlik bilgileri sağlar.

## 🌟 Özellikler
- **Tam IP Analizi** - Ülke, şehir, İSS ve daha fazlası
- **Güvenlik Kontrolleri** - Proxy/VPN/Tor çıkışlarını tespit edin
- **Zengin Görsel Çıktı** - Renkli konsol sunumu
- **Fallback Desteği** - Zengin kütüphane olmadan çalışır
- **Kolay Kurulum** - Otomatik bağımlılık kurulumu

## 📦 Kurulum
```bash
# Depoyu klonlayın
git clone https://github.com/exsarorrayzer/ipchecker.git
cd ipchecker

# Kurulumu çalıştır (bağımlılıkları otomatik yükler)
python setup.py
```

## 🚀 Kullanım
```bash
python main.py
```
Sonra ya:
- Aranacak bir IP adresi girin
- Kendi IP adresinizi kontrol etmek için Enter tuşuna basın

## 🛠️ Teknik Ayrıntılar
### Bağımlılıklar
- `requests` - API iletişimi için
- `rich` - Güzel konsol çıktısı için (isteğe bağlı)

### Dosya Yapısı
```
ipchecker/
├── main.py # Ana uygulama
├── setup.py # Kurulum Toolu
└── requirements.txt # Gerekli Kutuphaneler
```

## ⚠️ Önemli Notlar
- Ücretsiz ip-api.com limitleri: 45 istek/dakika
- Python 3.6+ gerektirir
- Windows/Linux/macOS/Android üzerinde çalışır
- Sadece eğitim amaçlı

## 📜 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır - s
 
