from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()

driver.get("https://qaproductrvw.ccbp.tech/product/")
driver.implicitly_wait(10)
review_btn=driver.find_element(By.CLASS_NAME,"review-btn")
review_btn.click()
time.sleep(5)
if driver.current_url=="https://qaproductrvw.ccbp.tech/review":
    print("Sucessfully redirected")
else:
    print("redirection failed")
rating_dropdown=driver.find_element(By.ID,"ratingSelect")
options=Select(rating_dropdown)
options.select_by_value("5")
review_content=driver.find_element(By.ID,"reviewTextArea")
review_content.send_keys( "Great quality, reasonable price, and high rating. Highly recommended!")
review_wait=WebDriverWait(driver,5)
review_btn=review_wait.until(EC.element_to_be_clickable((By.ID,"submitReviewBtn")))
review_btn.click()
time.sleep(2)
if(driver.current_url=="https://qaproductrvw.ccbp.tech/product"):
    print("Redirected to product page sucessfully")
else:
    print("Failed to submit")
time.sleep(3)