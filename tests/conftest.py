import pytest
from core.webdriver_setup import get_driver

@pytest.fixture
def driver():

    driver_instance = get_driver()

    yield driver_instance

    driver_instance.quit()