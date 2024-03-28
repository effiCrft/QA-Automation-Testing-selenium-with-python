import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("http://shop.icraftsoft.net:8095/")
driver.maximize_window()
time.sleep(3)#wait
driver.find_element(By.XPATH,"(//input[@class='btnSubmit'])[2]").click()
time.sleep(5)

driver.find_element(By.XPATH, "//input[contains(@name,'username')]").send_keys("Ephraim")
time.sleep(3)

driver.find_element(By.XPATH,"//input[@type='email']").send_keys("effi2andy@gmail.com")
time.sleep(3)

driver.find_element(By.XPATH,"//input[contains(@value,'Register')]").click()
time.sleep(10)


