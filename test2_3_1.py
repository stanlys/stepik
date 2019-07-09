from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select
import os 


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element_by_css_selector("button.btn")
button.click()
confirm = browser.switch_to.alert
confirm.accept()
num1 = browser.find_element_by_css_selector("#input_value").text
browser.find_element_by_css_selector("#answer").send_keys(calc(num1))
button = browser.find_element_by_css_selector("button.btn")
button.click()
