from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge()
driver.get(" https://qamarkskills.ccbp.tech/")
elements=driver.find_elements(By.CSS_SELECTOR,"li[class='p-1']>input[type='checkbox']")
labels=driver.find_elements(By.CSS_SELECTOR,"li[class='p-1']>label")

for i in range(len(elements)):
    elements[i].click()
    time.sleep(1)
    print(labels[i].text+" selected")
    elements[i].click()
    print("deselected successfully")
    time.sleep(1)
time.sleep(2)