from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver):

    print("\n[LOG] Login (Giriş) sayfasına gidiliyor...")
    driver.get("https://etiya-csm-ui-test2.etiya.com/login")

    login_sayfasi = LoginPage(driver)
    print("[LOG] Kullanıcı adı ve şifre giriliyor...")

    login_sayfasi.kullanici_adi_gir("csmadmin@etiya.com")
    login_sayfasi.sifre_gir("Csm123456!")
    login_sayfasi.giris_butonuna_tikla()

    wait = WebDriverWait(driver,10)
    wait.until(EC.url_contains("dashboard"))

    guncel_adres = driver.current_url
    assert "dashboard" in guncel_adres
    print("[LOG] Sisteme başarıyla giriş yapıldı. Test Geçti!")

def test_wrong_url(driver):

    driver.get("https://kitap.com/yanlis-sayfa")
    sayfa_metni = driver.page_source
    assert "404" in sayfa_metni or "Not Found" in sayfa_metni