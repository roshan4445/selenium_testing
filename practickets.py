from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver=webdriver.Chrome()
driver.get("https://qaconcertreg.ccbp.tech/")
name=driver.find_element(By.ID,"name")
name.send_keys("Charlie")
book_btn=driver.find_element(By.CLASS_NAME,"btn")
book_btn.click()
time.sleep(3)
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
email=driver.find_element(By.ID,"email")
email.send_keys("charlie@gmail.com")
book_btn.click()
alert_sucess=driver.switch_to.alert
print(alert_sucess.text)
alert_sucess.accept()
otp=driver.find_element(By.ID,"passcode")
otp.send_keys(123456)
verify_btn=driver.find_element(By.XPATH,"//button[text()='Verify']")
verify_btn.click()
check_alert=driver.switch_to.alert
print(check_alert.text)
time.sleep(1)
check_alert.accept()
sucessful_alert=driver.switch_to.alert 
time.sleep(1)
sucessful_alert.accept()
promocode_alert=driver.switch_to.alert
print(promocode_alert.text)
promocode_alert.send_keys("foodmunch")
time.sleep(1)
print("voucher issued")
promocode_alert.accept()







time.sleep(2)