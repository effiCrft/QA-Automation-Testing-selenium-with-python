import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()


driver.get("https://end-to-end-v1.onrender.com/registration/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH,"//input[@name='first_name']").send_keys("Ephraim")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='last_name']").send_keys("ANDE")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("EFIANDE")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("effiande@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='phone']").send_keys("+9805053227")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@type='date']").send_keys("03/24/2020")
time.sleep(1)
driver.find_element(By.XPATH,"//textarea[@name='address']").send_keys(".101 JhonSmith St,Cary.NC")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='password1']").send_keys("efiande")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='password2']").send_keys("efiande")
time.sleep(1)
driver.find_element(By.XPATH,"//select[@class='form-element']").send_keys("user")
time.sleep(1)

driver.find_element(By.XPATH,"//input[@value='Register']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//a[contains(.,'Login')]").click()
time.sleep(3)








