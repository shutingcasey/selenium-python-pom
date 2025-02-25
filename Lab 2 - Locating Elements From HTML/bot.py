
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# cService = webdriver.ChromeService(executable_path='C:\Program Files (x86)\chromedriver.exe')  
# driver = webdriver.Chrome(service = cService)

driver = webdriver.Chrome()
driver.get("https://www.senecapolytechnic.ca/search.html?q=")

# id --> name --> class name
search = driver.find_element(By.NAME, "q")

# type what you want to search
search.send_keys("Certificates")

# Enter
search.send_keys(Keys.RETURN)

try:
    id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"___gcse_0"))
    )
    divs = id.find_elements(By.TAG_NAME,"div")
    for div in divs:
        title = div.find_element(By.CLASS_NAME,"gs-title")
        print(title.text)

finally:
    driver.quit()

driver.quit()


