from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/monika.sharma/Desktop/selenium-with-python/drivers/chromedriver")

driver.get("http://www.google.com")
print(driver.title)