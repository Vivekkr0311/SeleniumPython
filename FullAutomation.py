from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Xpath can be delared gloabally.
FIRST_NAME_FIELD_XPATH = "//input[@id='fname']"
LAST_NAME_FIELD_XPATH = "//input[@id='lname']"
GENDER_MALE_RADIO_BUTTON_XPATH = "//input[@id='{gender}']"
OPTION_SELECT_XPATH = "//select[@name='option']/option[@value='option 1']"
MULTIPLE_OPTION_XPATH = "//select[@multiple='owc']/option[@value='option 1']"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def launchWebSite():
    driver.get("https://trytestingthis.netlify.app")
    print("[+] Website launched")

def makingUseOfXpath():
    firstName = driver.find_element(By.XPATH, FIRST_NAME_FIELD_XPATH)
    firstNameInput = input("[?] Can you give first name? : ")
    firstName.send_keys(firstNameInput)

    lastName = driver.find_element(By.XPATH, LAST_NAME_FIELD_XPATH)
    lastNameInput = input("[?] Can you give last name? : ")
    lastName.send_keys(lastNameInput)
    print("[+] Website is filled with your name.")

def selectOption():
    gender = input("[?] Give your gender: male/ female/ or /other: ")
    driver.find_element(By.XPATH, GENDER_MALE_RADIO_BUTTON_XPATH.format(gender=gender)).click()
    print("[+] Gender is selected")
    driver.find_element(By.XPATH, OPTION_SELECT_XPATH).click()
    print("[+] Option is selected")
    driver.find_element(By.XPATH, MULTIPLE_OPTION_XPATH).click()
    print("[+] Multiple option is selected")

if __name__ == "__main__":
    launchWebSite()
    makingUseOfXpath()
    selectOption()
    time.sleep(10)
    print("[+] Automation script working fine.")
    driver.quit()