from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(30)

    driver.implicitly_wait(10)

    return driver


if __name__ == "__main__":
    print("Chrome başlatılıyor...")
    deneme_driver = get_driver()
    deneme_driver.get("https://www.google.com")
    print("Başarılı! Chrome açıldı. 5 saniye sonra kapanacak...")

    import time

    time.sleep(5)
    deneme_driver.quit()