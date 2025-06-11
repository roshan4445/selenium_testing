from selenium import webdriver
from selenium.webdriver.common.by import By
import time
niatdriver=webdriver.Chrome()
niatdriver.implicitly_wait(10)
niatdriver.get("https://www.bing.com")
search_bar=niatdriver.find_element(By.ID,"sb_form_q")
search_bar.send_keys("AlluArjun biography")
search_btn=niatdriver.find_element(By.ID,"search_icon")
search_btn.click()
time.sleep(10)
