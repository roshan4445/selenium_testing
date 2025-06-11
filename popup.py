from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
popdriver=webdriver.Chrome()
popdriver.implicitly_wait(10)
popdriver.get("https://the-internet.herokuapp.com/javascript_alerts")
jspopbtn=popdriver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")
jspopbtn.click()

alert=popdriver.switch_to.alert
alert.accept()
jsconfirmpopup=popdriver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']")
jsconfirmpopup.click()

confirmalert=popdriver.switch_to.alert
confirmalert.dismiss()
jsconfirmpopup=popdriver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']")
jsconfirmpopup.click()
time.sleep(5)
promptpop=popdriver.switch_to.alert
promptpop.send_keys("Roshan")
promptpop.accept()

time.sleep(20)