from selenium import webdriver
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

num1 = browser.find_element_by_css_selector("#input_value").text
num2 = calc(num1)
inputname = browser.find_element_by_css_selector("#answer")
inputname.send_keys(str(num2))
button = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
robot1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
robot1.click()
robot1 = browser.find_element_by_css_selector("[value='robots']")
robot1.click()


button.click()
