from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(3)  

modal_close_button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer")
modal_close_button.click()

sleep(10)

driver.quit()