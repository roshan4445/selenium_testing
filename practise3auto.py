from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://qawikisearch.ccbp.tech/")
search_input=driver.find_element(By.XPATH,"//input[@id='searchInput']")
search_input.send_keys("India")
search_btn=driver.find_element(By.XPATH,"//button[@id='submitButton']")
search_btn.click()
time.sleep(10)