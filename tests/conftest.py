import pytest
from core.webdriver_setup import get_driver
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():

    driver_instance = get_driver()

    yield driver_instance

    driver_instance.quit()

@pytest.fixture
def authenticated_driver(driver):
    # 1. Login sayfasına git ve giriş yap
    driver.get("https://example.com/login")
    login_sayfasi = LoginPage(driver)
    login_sayfasi.kullanici_adi_gir("ornek.com")
    login_sayfasi.sifre_gir("123456")
    login_sayfasi.giris_butonuna_tikla()

    # 2. Girişin başarılı olduğunu doğrula ve sayfanın yüklenmesini bekle
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))

    # 3. İçeride hazır bulunan (Login olmuş) driver'ı testlere teslim et
    yield driver
