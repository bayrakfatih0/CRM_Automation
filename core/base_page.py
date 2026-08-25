import os.path
import time
from datetime import datetime
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def find_element(self, locator):
        # Elementin sayfada görünür olmasını bekler
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        # Elementin tıklanabilir olmasını bekler ve tıklar
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        # Elementi bulur, içini temizler ve metni yazar
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def slow_enter_text(self, locator, text, delay=0.1):
        element = self.find_element(locator)
        element.clear()
        for char in text:
            element.send_keys(char)
            time.sleep(delay)

    def smart_click(self,locator, retries=3):
        for attempt in range(retries):
            try:
                element = self.wait.until((EC.element_to_be_clickable(locator)))
                self.driver.execute_script("arguments[0].click()",element)
                return
            except (StaleElementReferenceException,TimeoutException):
                if attempt == retries - 1:
                    raise
                time.sleep(0.5)

    def take_screenshot(self, name_prefix="screenshot"):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath  = f"screenshots/{name_prefix}_{timestamp}.png"

        self.driver.save_screenshot(filepath)
        print(f"Ekran görüntüsü alındı... {filepath}")