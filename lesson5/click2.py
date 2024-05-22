from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

service = ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("http://uitestingplayground.com/classattr")

blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn class3 btn-primary btn-test")
blue_button.click()

for _ in range(3):
    
    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn class3 btn-primary btn-test")
    blue_button.click()
    sleep(1)

driver.quit()
