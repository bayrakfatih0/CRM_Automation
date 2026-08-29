from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.dashboard import Dashboard
import time

def test_ticket_create(driver):

    # Login
    driver.get("https://etiya-csm-ui-test2.etiya.com/login")
    login_sayfasi = LoginPage(driver)
    login_sayfasi.kullanici_adi_gir("csmadmin@etiya.com")
    login_sayfasi.sifre_gir("Csm123456!")
    login_sayfasi.giris_butonuna_tikla()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("dashboard"))
    print("Login olunmuştur.")
    time.sleep(3)
    # Ticket Create sayfasına giriş
    dashboard = Dashboard(driver)
    dashboard.ticket_page()
    dashboard.ticket_create_button()
    dashboard.fill_firstname("8888")
    dashboard.search_customer()
    dashboard.find_customer("8888")
    print("Create ticket sayfasına gelmiştir.")

    # Ticket Create işlemi
    dashboard.fill_channel("Channel en")
    dashboard.fill_ticket_type("ayltest")
    dashboard.fill_category("Category e")
    dashboard.fill_sub_category("bcategories")
    dashboard.fill_priority("Low")
    dashboard.description("Test açıklamasıdır.")
    dashboard.create_ticket()
    print("işlem tamamlandı, ticket create başarılı...")

    is_redirected = dashboard.wait_for_url_contains("tickets")

    assert is_redirected, f"Kayıt sonrası yönlendirme başarısız! Mevcut URL: {driver.current_url}"
    print("İşlem başarılı, sistem yeni biletin sayfasına sorunsuzca yönlendirildi.")