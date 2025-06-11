from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://qaebank.ccbp.tech/ebank/login")
username=driver.find_element(By.CLASS_NAME,"input-field")
username.send_keys(142420)
password=driver.find_element(By.ID,"pinInput")
password.send_keys(231225)
time.sleep(2)
login_btn=driver.find_element(By.CLASS_NAME,"login-button")
login_btn.click()
print("Submitted_logindetails")
if(driver.current_url=="https://qaebank.ccbp.tech/ebank"):
    print("Logged in sucessfully")
    print(driver.title)
else:
    print("Login unSucessfull")
time.sleep(10)
logout_btn=driver.find_element(By.CLASS_NAME,"logout-button")
logout_btn.click()
if(driver.current_url=="https://qaebank.ccbp.tech/ebank/login"):
    print("Logged out sucessfully")
time.sleep(10)
