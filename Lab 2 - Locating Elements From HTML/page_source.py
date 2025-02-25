
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.senecapolytechnic.ca/search.html?q=")

# id --> name --> class name
search = driver.find_element(By.NAME, "q")

# type what you want to search
search.send_keys("Certificates")

# Enter
search.send_keys(Keys.RETURN)

print(driver.page_source)

time.sleep(5)


