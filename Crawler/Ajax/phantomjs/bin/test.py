from selenium import webdriver
import time

driver = webdriver.PhantomJS()

driver.get("https://gist.githubusercontent.com/garyherd/67adc751c743774b46a0/raw/67b264f3ccbba88d1014fa31182916482b07056b/simple_caesar_encryption.py")
time.sleep(3)

print(driver.text)

driver.close()
