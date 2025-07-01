from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://qaflightbooking.ccbp.tech/")
departure_city=driver.find_element(By.ID,"departureCity")
departure_city.send_keys("New York")
arrival_city=driver.find_element(By.ID,"destinationCity")
arrival_city.send_keys("Los Angels")
departure_date=driver.find_element(By.ID,"travelDate")
departure_date.send_keys("01/08/2023")
no_of_passengers=driver.find_element(By.ID,"passengers")
no_of_passengers.send_keys("2")
wait=WebDriverWait(driver,5)
search_btn = wait.until(EC.element_to_be_clickable((By.ID, "searchBtn")))

search_btn.click()
flight=driver.find_element(By.CSS_SELECTOR,"input[value='0']")
flight.click()
wait_book=WebDriverWait(driver,5)
booknow_btn=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='container']>button")))
booknow_btn.click()
password_input=driver.find_element(By.CSS_SELECTOR,"div[class='container']>input[type='password']")
password_input.send_keys("traveler123")
paynow_btn=driver.find_element(By.CSS_SELECTOR,"div[class='container']>button")
paynow_btn.click()
sucess_wait=WebDriverWait(driver,5)
sucessful_msg=sucess_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[class='container']>h2")))
if sucessful_msg.text!="":
    print("Booking sucessfull")
else:
    print("Booking failed")




time.sleep(2)