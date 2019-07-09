from selenium import webdriver
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)

num1 = browser.find_element_by_css_selector("#num1").text
num2 = browser.find_element_by_css_selector("#num2").text

num3 = int(num1)+int(num2)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(num3)) # ищем элемент с текстом "Python"

button = browser.find_element_by_css_selector("button.btn")
button.click()
