import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('index', ["895", "896","897","898","899","903","904","905"])
def test_guest_should_see_login_link(browser,index):
    link = "https://stepik.org/lesson/236{}/step/1".format(index)
    #link = "https://stepik.org/lesson/236895/step/1"
    print(link)
    browser.get(link)
    textarea = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )
    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))
    button = browser.find_element_by_css_selector(".submit-submission")
    button = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "button"))
    )
    button.click()
    time.sleep(1)
    text = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert "Correct!" == text, "SEE HERE -"
