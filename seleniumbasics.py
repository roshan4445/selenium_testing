from selenium import webdriver
from selenium.wendriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://github.com/")
input_element=driver.find_element(By.Id,"ap_email_login")
input_element.send_keys(9703586074)
continue_button=driver.find_element(By.CLASS_NAME,"a-button-input")
continue_button.click()


time.sleep(10)
