from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(option)
driver.maximize_window()

url = "https://saucedemo.com"
driver.get (url)

driver.find_element(By.ID,"user-name").send_keys("problem_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()

sleep(5)

driver.quit()
