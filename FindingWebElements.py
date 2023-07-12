from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://google.com")

#This below line is used to locate web element using their web element name.
search_bar = driver.find_element(By.NAME, "q")
print("[+] Web element found.")
search_bar.send_keys("Github")
print("[+] Github text sent to web element.")
search_bar.send_keys(Keys.RETURN)
print("[+] Return is hit")

time.sleep(5)
print("[+] Automation script working fine.")
driver.quit()