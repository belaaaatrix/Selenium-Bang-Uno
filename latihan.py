from selenium import webdriver
from time import sleep


option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)


driver = webdriver.Chrome(option)
driver.maximize_window()


driver.get ("https://tiket.com")
print(driver.title)

driver.get("https://kelasotomesyen.com")
print(driver.title)


driver.back()
print(driver.title)
sleep(5)

driver.quit()