# CRM Automation Framework 🚀

Bu proje, CRM sistemleri üzerinde talep oluşturma süreçlerini otomatize etmek amacıyla geliştirilmiş, **Python**, **Selenium** ve **LLM (Büyük Dil Modelleri)** destekli uçtan uca (E2E) bir test otomasyon çerçevesidir. 60 farklı senaryoyu (case) kapsayacak şekilde kurumsal standartlarda tasarlanmıştır.

## 🎯 Projenin Amacı ve Temel Özellikler

*   **Page Object Model (POM):** Sürdürülebilir, modüler ve kod tekrarından arındırılmış mimari.
*   **LLM Entegrasyonu:** Test verilerini dinamik olarak üretmek ve kompleks karar mekanizmalarını yönetmek için akıllı asistan desteği.
*   **İleri Düzey Performans:** `pytest-xdist` ile paralel koşum, `pytest-rerunfailures` ile kararsız (flaky) testlere karşı otomatik kurtarma yeteneği.
*   **Görsel ve Detaylı Raporlama:** **Allure Report** entegrasyonu sayesinde her adımın, ekran görüntüsünün, video kayıtlarının (FFmpeg) ve ağ loglarının (Selenium-Wire) kaydedildiği interaktif metrik panelleri.
*   **CI/CD Hazır (DevOps):** **Docker** ile izole ortam garantisi ve **Jenkins** Pipeline (Cron/Zamanlanmış) desteği.

---

## 🏗️ Mimari ve Klasör Yapısı

Proje spagetti koddan uzak, kolay taşınabilir bir yapıda inşa edilmiştir:

```text
SeleniumCSMProject/
├── core/               # WebDriver ayarları, BasePage metodları ve LLM API yöneticisi
├── data/               # Test verileri, senaryolar ve LLM prompt taslakları
├── pages/              # Web sayfalarını temsil eden sınıflar ve Locator'lar
├── tests/              # pytest formatında yazılmış test senaryoları
├── allure-results/     # Allure raporlarının tutulduğu dizin (Dinamik oluşturulur)
├── conftest.py         # Pytest fixture (Driver setup, video kaydı vb.) yapılandırmaları
├── Jenkinsfile         # CI/CD otomasyon hattı tanımları
├── Dockerfile          # Headless ortam konfigürasyonu
├── requirements.txt    # Proje bağımlılıkları
└── .env                # (Git'e eklenmez) API key, şifre ve hassas veriler
```
⚙️ Kurulum ve Çalıştırma
Yerel Ortam (Local)
Projeyi klonlayın ve klasöre girin:

Bash
git clone [https://github.com/KULLANICI_ADIN/CRM_Automation.git](https://github.com/bayrakfatih0/CRM_Automation)
cd CRM_Automation

Sanal ortamı oluşturun ve aktif edin:
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

Gereksinimleri yükleyin:
pip install -r requirements.txt
Proje dizininde bir .env dosyası oluşturup LLM anahtarınızı girin:
Kod snippet'i
LLM_API_KEY=senin_gizli_anahtarin

Testleri çalıştırın (Paralel, Rerun ve Allure desteği ile):
pytest tests/ -n auto --reruns 3 --reruns-delay 2 --alluredir=allure-results

Allure Raporunu Görüntüleyin:
allure serve allure-results

Docker Üzerinde Çalıştırma
Proje bilgisayarınızda arayüz açmadan izole bir konteyner içinde koşacak şekilde ayarlanmıştır:

İmajı inşa edin:
docker build -t crm-automation .
Konteyneri başlatın (Raporların ana bilgisayara kaydedilmesi için workspace volume'u bağlıdır):
docker run --rm -v ${PWD}/allure-results:/app/allure-results -e LLM_API_KEY="key"
