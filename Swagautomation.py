from selenium import webdriver
from selenium.webdriver.common.by import By
import time

swagdriver=webdriver.Chrome()
swagdriver.implicitly_wait(10)
swagdriver.get("https://www.saucedemo.com/")
username_input=swagdriver.find_element(By.XPATH,"//input[@id='user-name']")
username_input.send_keys("standard_user")
password_input=swagdriver.find_element(By.XPATH,"//input[@id='password']")
password_input.send_keys("secret_sauce")
loginbtn=swagdriver.find_element(By.XPATH,"//button[@id='login-button']")
loginbtn.click()
time.sleep(10)