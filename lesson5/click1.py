from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary"))) 

blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
blue_button.click()

for _ in range(3):
   
    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    blue_button.click()
    sleep(1)

driver.quit()
