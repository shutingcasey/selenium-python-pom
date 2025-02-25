from selenium import webdriver

cService = webdriver.ChromeService(executable_path='C:\Program Files (x86)\chromedriver.exe')  
driver = webdriver.Chrome(service = cService)

driver.get("https://www.ontario.ca/page/ministry-public-and-business-service-delivery-and-procurement")

# Web Scraping（網頁爬取）
print(driver.title)
driver.quit()