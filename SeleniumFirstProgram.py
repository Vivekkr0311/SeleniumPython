from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#Below line download chromedriver binary in default location.
#On Mac it is: /Users/{your_username}/.wdm/drivers/chromedriver/mac64/{chromedriver_version}/chromedriver

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://google.com")
print("[+] Working fine.")
time.sleep(5)
driver.quit()