
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
# upgrade the expensive one first

# price = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.ID, "productPrice0"), "")
# )
# items = [driver.find_element(By.ID, f"productPrice{i}") for i in range(0, 1, 1)]

driver.implicitly_wait(5)
select = driver.find_element(By.ID,"langSelect-EN")
select.click()

actions = ActionChains(driver)

try:
    price = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "productPrice0"), "")
    )
    actions.click(cookie)
    for i in range(100):
        actions.perform()
    time.sleep(5)
except:
    driver.quit()


driver.quit()










# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time