from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
driver=webdriver.Edge()
driver.get("https://qafitnesslib.ccbp.tech/")
driver.implicitly_wait(10)
types_btn=driver.find_elements(By.CSS_SELECTOR,"li[class='category-item']")
for type in types_btn:
    type.click()
    wait=WebDriverWait(driver,5)
    exercises=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"div[id='exerciseList']>div")))
    if(exercises):
        for exercise in exercises:
            exercise.click()
            time.sleep(2)
            title_wait=WebDriverWait(driver,5)
            title=title_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='exercise-details-container']>h3")))
            print(title.text+"is selected")
            description_wait=WebDriverWait(driver,10)
            description=description_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div[class='exercise-details-container']>p")))
            print(description.text)


    

time.sleep(5)