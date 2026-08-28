import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from core.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class Dashboard(BasePage):

    TICKET_PAGE = (By.XPATH, "//a[@href='/tickets']")
    CREATE_TICKET_PAGE = (By.XPATH, "//a[@href='/tickets/create']")
    FIRSTNAME = (By.ID, "firstName")
    SEARCH = (By.XPATH, "//button[@type='submit']")
    CUSTOMER = (By.XPATH, "//div[@row-id='{customer_id}']")

    EDITOR_IFRAME = (By.CSS_SELECTOR, "iframe.fr-iframe")
    EDITOR_METIN = (By.CSS_SELECTOR, "body.fr-view")
    CHANNEL = (By.NAME, "channel")
    TICKETTYPE = (By.NAME, "ticketType")
    CATEGORY = (By.NAME, "category")
    SUBCATEGORY = (By.NAME, "subCategory")
    PRIORITY = (By.NAME, "priority")
    CREATE_TICKET = (By.XPATH, "//atom-button[@id='create-ticket']/button")
    SUCCESS_POPUP = (By.XPATH, "//p[contains(text(), 'Ticket has been created')]")

    def __init__(self, driver):
        super().__init__(driver)

    def ticket_page(self):
        self.click_element(self.TICKET_PAGE)

    def ticket_create_button(self):
        self.click_element(self.CREATE_TICKET_PAGE)

    def fill_firstname(self, firstname: str):
        self.slow_enter_text(self.FIRSTNAME, firstname)

    def search_customer(self):
        self.click_element(self.SEARCH)

    def find_customer(self, customer_id):
        customer_locator = (By.XPATH, f"//div[@row-id='{customer_id}']")
        self.smart_click(customer_locator)

    def description(self, metin: str):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.EDITOR_IFRAME))
        try:
            body_element = self.wait.until(EC.element_to_be_clickable(self.EDITOR_METIN))
            actions = ActionChains(self.driver)
            actions.move_to_element(body_element).click().pause(0.5).send_keys(metin).perform()
            actions.send_keys(Keys.SPACE).send_keys(Keys.BACKSPACE).perform()
        finally:
            self.driver.switch_to.default_content()
        time.sleep(1)
        #self.take_screenshot("iframe_metin_yazildi")

    def fill_channel(self, channel_name:str):
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(0.5)
        input_element = self.find_element(self.CHANNEL)
        self.driver.execute_script("arguments[0].click();", input_element)
        input_element.send_keys(channel_name)
        time.sleep(1)
        option_locator = (By.XPATH, f"//span[normalize-space(text())='{channel_name}']")
        self.smart_click(option_locator)


    def fill_ticket_type(self, tickettype: str):
        input_element = self.find_element(self.TICKETTYPE)
        actions = ActionChains(self.driver)
        actions.move_to_element(input_element).click().send_keys(tickettype).perform()
        time.sleep(1)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        option_locator = (By.XPATH, f"//span[normalize-space(text())='{tickettype}']")
        self.smart_click(option_locator)

    def fill_category(self, category: str):
        input_element = self.find_element(self.CATEGORY)
        actions = ActionChains(self.driver)
        actions.move_to_element(input_element).click().send_keys(category).perform()
        time.sleep(1)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        option_locator = (By.XPATH, f"//span[normalize-space(text())='{category}']")
        self.smart_click(option_locator)

    def fill_sub_category(self, subcategory: str):
        input_element = self.find_element(self.SUBCATEGORY)
        actions = ActionChains(self.driver)
        actions.move_to_element(input_element).click().send_keys(subcategory).perform()
        time.sleep(1)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        option_locator = (By.XPATH, f"//span[normalize-space(text())='{subcategory}']")
        self.smart_click(option_locator)

    def fill_priority(self, priority: str):
        input_element = self.find_element(self.PRIORITY)
        actions = ActionChains(self.driver)
        actions.move_to_element(input_element).click().send_keys(priority).perform()
        time.sleep(1)
        actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        option_locator = (By.XPATH, f"//span[normalize-space(text())='{priority}']")
        self.smart_click(option_locator)

    def create_ticket(self):
        self.smart_click(self.CREATE_TICKET)

    def get_success_message(self):
        popup_element = self.find_element(self.SUCCESS_POPUP)
        self.take_screenshot("Create ticket edildi")
        return popup_element.text

    def wait_for_url_contains(self, partial_url):
        try:
            # Mevcut URL'in beklediğimiz kelimeyi içermesini belirtilen süre kadar bekler
            self.wait.until(EC.url_contains(partial_url))
            return True
        except TimeoutException:
            return False






