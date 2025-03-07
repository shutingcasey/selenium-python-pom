from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePageElement(object):
    
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.locator))
        )
        driver.find_element(By.NAME, self.locator).clear()
        driver.find_element(By.NAME, self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.locator))
        )
        element = driver.find_element(By.NAME, self.locator)
        return element.get_attribute("value")
