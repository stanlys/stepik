from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select
import os 


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
button1 = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000 RUR")
    )
button = browser.find_element_by_css_selector("button.btn")
button.click()
bsolve = browser.find_element_by_css_selector("#solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", bsolve)

#button = browser.find_element_by_css_selector("button.btn")
#button.click()

#swith to new window
#browser.switch_to.window(browser.window_handles[1])
#button = browser.find_element_by_css_selector("button.btn")
#button.click()
num1 = browser.find_element_by_css_selector("#input_value").text
browser.find_element_by_css_selector("#answer").send_keys(calc(num1))

bsolve.click()
