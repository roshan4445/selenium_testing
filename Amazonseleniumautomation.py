from selenium import webdriver
from selenium.webdriver.common.by import By
import time

amazon_driver=webdriver.Chrome()
amazon_driver.implicitly_wait(30)
amazon_driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
input_number=amazon_driver.find_element(By.ID,"ap_email")
input_number.send_keys(9703586074)
continue_button=amazon_driver.find_element(By.CLASS_NAME,"a-button-input")
continue_button.click()
input_password=amazon_driver.find_element(By.ID,"ap_password")
input_password.send_keys("Khuddus@4445")
signin_button=amazon_driver.find_element(By.ID,"signInSubmit")
signin_button.click()
time.sleep(10)