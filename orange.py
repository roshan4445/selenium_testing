from selenium import webdriver
from selenium.webdriver.common.by import By
import time
orangedriver=webdriver.Chrome()
orangedriver.implicitly_wait(20)
orangedriver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
input_element=orangedriver.find_element(By.CSS_SELECTOR,"input[name='username']")
input_element.send_keys("Admin")
password_input=orangedriver.find_element(By.CSS_SELECTOR,"input[name='password']")
password_input.send_keys("admin123")
login_btn=orangedriver.find_element(By.CSS_SELECTOR,"button[type='submit']")
login_btn.click()
time.sleep(10)