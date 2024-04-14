from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By


service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)


driver.get("https://www.google.com")
driver.maximize_window()
# element = driver.find_element(By.TAG_NAME, "h1").get_attribute("innerHTML")
google_search = driver.find_element(By.NAME, "q")
google_search.clear()
google_search.send_keys("selenium python")
google_search.submit()

driver.close()
# driver.quit()


# assert "Google" in driver.title
# print(driver)
