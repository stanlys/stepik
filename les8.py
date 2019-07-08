from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_css_selector('.form-group #input_value')
x = x_element.text
y = calc(x)
inputname = browser.find_element_by_css_selector("#answer")
inputname.send_keys(str(y))
robot1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
robot1.click()
robot1 = browser.find_element_by_css_selector("[value='robots']")
robot1.click()
# Ваш код, который заполняет обязательные поля
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()


