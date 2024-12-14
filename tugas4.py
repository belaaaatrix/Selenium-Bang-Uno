from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)


driver = webdriver.Chrome(option)
driver.minimize_window()


urls = [
    "https://tiket.com",
    "https://tokopedia.com",
    "https://orangsiber.com",
    "https://idejongkok.com",
    "https://kelasotomesyen.com",
]

# Loop untuk mengambil title setiap URL
try:
    for url in urls:
        driver.get(url)  
        print(url, "-", driver.title)
finally:
    driver.quit()  