from selenium import webdriver
import time
driver=webdriver.Chrome("chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_id("fakebox-text").send_keys("javatpoint")  
time.sleep(3)
driver.find_element_by_class_name("search-icon").send_keys(Keys.ENTER)  
time.sleep(3)
driver.close()