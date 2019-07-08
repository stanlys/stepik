from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(float(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
x = browser.find_element_by_css_selector('#treasure').get_attribute("valuex")
print(x)
y = calc(x)
inputname = browser.find_element_by_css_selector("#answer")
inputname.send_keys(str(y))
robot1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
robot1.click()
robot1 = browser.find_element_by_css_selector("[value='robots']")
robot1.click()
# Ваш код, который заполняет обязательные поля
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()


