import pytest
from selenium.webdriver import Firefox

URL="http://www.cineca.it"
SEARCH_BOX_ID="edit-search-block-form--2"

@pytest.fixture(scope='function')
def driver():
    driver = Firefox()
    yield driver
    driver.quit()

def test_search(driver):
    driver.get(URL)
    driver.find_element_by_id(SEARCH_BOX_ID)
