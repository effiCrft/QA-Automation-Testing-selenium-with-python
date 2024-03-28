from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://shop.icraftsoft.net:8095/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@type='number']").send_keys("3680")
time.sleep(4)

driver.find_element(By.XPATH,"//input[contains(@value,'Login')]").click()
time.sleep(1)
driver.find_element(By.XPATH,"(//button[@data-toggle='modal'])[2]").click()
time.sleep(2)

# To chose Quantity
driver.find_element(By.XPATH,"(//select[@name='quantity'])[2]").send_keys("3")
time.sleep(2)

# To Add cart
driver.find_element(By.XPATH,"(//button[contains(.,'Add to cart')])[32]").click()
time.sleep(2)

# To view cart
driver.find_element(By.XPATH,"//a[contains(.,'Cart (2)')]").click()
time.sleep(5)

# To buy
driver.find_element(By.XPATH,"//input[@value='Buy Now']").click()
time.sleep(3)











