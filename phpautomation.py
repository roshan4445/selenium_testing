from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
netflixdriver=webdriver.Chrome()
netflixdriver.implicitly_wait(10)
netflixdriver.get("https://www.netflix.com/in/")
email_input=netflixdriver.find_element(By.ID,":r13:")
email_input.send_keys("rzameerr115@gmail.com")
getstarted_btn=netflixdriver.find_element(By.CSS_SELECTOR,".pressable_styles__a6ynkg0.button_styles__1kwr4ym0.default-ltr-cache-xh7a98-StyledBaseButton.e1ax5wel2")
getstarted_btn.click()
input_password=netflixdriver.find_element(By.ID,"id_password")
input_password.send_keys("Khuddus@4445")
time.sleep(10)