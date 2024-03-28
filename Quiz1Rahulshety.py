import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='enter-name']").send_keys("ephraim")
time.sleep(2)
#driver.find_element(By.XPATH,"//input[@value='Alert']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@value='Confirm']").click()
time.sleep(2)