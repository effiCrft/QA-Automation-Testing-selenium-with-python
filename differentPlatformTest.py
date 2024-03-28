import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#browse url
driver.get("https://www.google.com/")
driver.maximize_window()
time.sleep(3)

#driver
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(3)
#driver
driver.get("https://www.amazon.com/")
driver.maximize_window()
time.sleep()




















































