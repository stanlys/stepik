from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select
import os 


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
browser.find_element_by_css_selector("[name='firstname']").send_keys("Stan")
browser.find_element_by_css_selector("[name='lastname']").send_keys("Stanlys")
browser.find_element_by_css_selector("[name='email']").send_keys("Stanlys@yandex.ru")
browser.find_element_by_css_selector("[name='file']").send_keys(file_path)
button = browser.find_element_by_css_selector("button.btn")
button.click()
