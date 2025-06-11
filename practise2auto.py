from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://qabloglist.ccbp.tech/")
time.sleep(2)
about=driver.find_element(By.XPATH,"//a[@href='/about']")
about.click()
if(driver.current_url=="https://qabloglist.ccbp.tech/about"):
    print("Navigated to about page")
else:
    print("Navigation to about page failed")
time.sleep(2)
contact=driver.find_element(By.XPATH,"//a[@href='/contact']")
contact.click()
if(driver.current_url=="https://qabloglist.ccbp.tech/contact"):
    print("Navigated to Contact page")
else:
    print("Navigation to Contact page failed")

time.sleep(2)
home=driver.find_element(By.XPATH,"//a[@href='/']")
home.click()
if(driver.current_url=="https://qabloglist.ccbp.tech/"):
    print("Navigated to Home page")
else:
    print("Navigation to Home page failed")
time.sleep(2)

