from selenium import webdriver
from selenium.webdriver.common.by import By
import time

flipkartdriver=webdriver.Chrome()
flipkartdriver.implicitly_wait(20)
flipkartdriver.get("https://www.flipkart.com/account/login?ret=/account/login%3Fret%3D%2F")
number_input=flipkartdriver.find_element(By.CSS_SELECTOR, ".r4vIwl.BV\\+Dqf")
number_input.send_keys(9703586074)
otp_button=otp_button = flipkartdriver.find_element(By.CSS_SELECTOR, ".QqFHMw.twnTnD._7Pd1Fp")
otp_button.click()
otp=int(input())

time.sleep(10)