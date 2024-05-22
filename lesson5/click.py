from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

service = ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    add_element_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    add_element_button.click()

delete_buttons = driver.find_elements(By.CSS_SELECTOR, "button.added-manually")


print("Размер списка кнопок 'Delete':", len(delete_buttons))

driver.quit()
