from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://students.senecapolytechnic.ca/")

link = driver.find_element(By.LINK_TEXT,"Academic")
link.click()
time.sleep(5)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='Accessible Learning Services']"))
    )
    element.click()
    time.sleep(5)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Who We Are"))
    )
    element.click()
    time.sleep(5)

    driver.back()
    driver.back()
    driver.back()
    time.sleep(5)
    driver.forward()
    time.sleep(5)
except:
    driver.quit()