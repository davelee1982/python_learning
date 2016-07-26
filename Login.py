#Webmail Login

#Import
import time
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys

#Definitions
def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None
driver = webdriver.Firefox()
driver.get("http://northsandiegomonart.com:2095")
wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)
email_field = driver.find_element_by_id("user")
email_field.send_keys("info@northsandiegomonart.com")
password_field = driver.find_element_by_id("pass")
password_field.send_keys("sbmonart")
password_field.send_keys(Keys.RETURN)

input()
