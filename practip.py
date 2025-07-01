from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver=webdriver.Chrome()
driver.get("https://qatipcalc.ccbp.tech/")
driver.implicitly_wait(10)
bill_amount_input=driver.find_element(By.CSS_SELECTOR,"input[class^='user-input']")
bill_amount_input.send_keys(1000)
percencentage_tip_bill=driver.find_element(By.CSS_SELECTOR,"input[id^='percentageTip']")
percencentage_tip_bill.send_keys(12)
time.sleep(2)
caluculate_button=driver.find_element(By.CSS_SELECTOR,"button[id^='calculateButton']")
caluculate_button.click()
time.sleep(2)
tip_amount_bill=driver.find_element(By.CSS_SELECTOR,"p[id^='tipAmount']")
expected_tip_amount=120
total_amount=driver.find_element(By.CSS_SELECTOR,"p[id^='totalAmount']")
expected_amount=1120
if(float(tip_amount_bill.text)==expected_tip_amount) and float(total_amount.text)==expected_amount:
    print("tip caluculated sucessfully")
else:
    print("Tip Calculated Incorrectly")
percencentage_tip_bill.clear()
caluculate_button.click()
time.sleep(2)
error_msg=driver.find_element(By.ID,"errorMessage")
if((error_msg.text)!=""):
    print("Error msg dispalyed sucessfully for empty input")
else:
    print("No Error Msg Displayed")
percencentage_tip_bill.clear()
percencentage_tip_bill.send_keys(20)
bill_amount_input.clear()
bill_amount_input.send_keys(1000)
caluculate_button.click()
time.sleep(2)
percencentage_tip_bill.clear()
percencentage_tip_bill.send_keys("10f")
caluculate_button.click()
if((error_msg.text)!=""):
    print("Error msg dispalyed sucessfully for invalid input")
else:
    print("No Error Msg Displayed")

time.sleep(3)
