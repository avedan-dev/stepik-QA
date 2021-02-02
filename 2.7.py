from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )

button1 = browser.find_element_by_id("book")
button1.click()

x = browser.find_element_by_id('input_value').text
y = math.log(abs(12*math.sin(int(x))))
ans = browser.find_element_by_id('answer')
ans.send_keys(str(y))

button2 = browser.find_element_by_css_selector('[type="submit"]')
button2.click()

time.sleep(15)
browser.quit()
