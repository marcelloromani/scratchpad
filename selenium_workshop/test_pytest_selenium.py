import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope='session')
def base_url():
    return "http://the-internet.herokuapp.com"

@pytest.mark.nondestructive
def test_login(base_url, selenium):
    selenium.get('{0}/login'.format(base_url))
    selenium.find_element(By.ID, "username").send_keys("admin")
    selenium.find_element(By.ID, "password").send_keys("admin")
    selenium.find_element(By.CSS_SELECTOR, "#login .fa-sign-in").click()
