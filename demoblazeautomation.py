from selenium import webdriver
from selenium.webdriver.common.by import By
import time
demoblazedriver=webdriver.Chrome()
demoblazedriver.implicitly_wait(10)
demoblazedriver.get("https://www.demoblaze.com/")
login_link=demoblazedriver.find_element(By.ID,"login2")
login_link.click()
username_input=demoblazedriver.find_element(By.ID,"loginusername")
username_input.send_keys("roshan_666")
password_input=demoblazedriver.find_element(By.ID,"loginpassword")
password_input.send_keys("Khuddus@4445")
login_btn=demoblazedriver.find_element(By.CSS_SELECTOR,'button[onclick="logIn()"]')
login_btn.click()
time.sleep(10)