import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://end-to-end-v1.onrender.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("efiande")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("effimon")
time.sleep(1)
driver.find_element(By.XPATH,"//button[@id='button']").click()
time.sleep(5)
