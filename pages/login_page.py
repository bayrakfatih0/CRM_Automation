from selenium.webdriver.common.by import By
from core.base_page import BasePage

class LoginPage(BasePage):

    KULLANICI_ADI_INPUT = (By.ID, "userName")
    SIFRE_INPUT = (By.ID, "password")
    GIRIS_BUTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    # --- ACTIONS (Aksiyon Metotları) ---
    def kullanici_adi_gir(self, kullanici_adi: str):
        """Kullanıcı adı alanına metin yazar."""
        element = self.driver.find_element(*self.KULLANICI_ADI_INPUT)
        element.clear()
        element.send_keys(kullanici_adi)

    def sifre_gir(self, sifre: str):
        """Şifre alanına metin yazar."""
        element = self.driver.find_element(*self.SIFRE_INPUT)
        element.clear()
        element.send_keys(sifre)

    def giris_butonuna_tikla(self):
        """Giriş yap butonuna tıklar."""
        element = self.driver.find_element(*self.GIRIS_BUTON)
        element.click()