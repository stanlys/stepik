from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
inputname = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
inputname.send_keys("Stan")
inputsurname = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
inputsurname.send_keys("Stanlys")
inputemail = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
inputemail.send_keys("Stan@bk.ru")
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

