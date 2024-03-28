import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)

# handle alert
driver.find_element(By.XPATH, "//input[@id='alertbtn']").click()
time.sleep(2)

alertPage = driver.switch_to.alert  # used to move or switch from real browser to pop message box page

time.sleep(8)
message = alertPage.text
print(message)

alertPage.accept()
