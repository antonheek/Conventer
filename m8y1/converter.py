from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def conv(val_1, val_2, count):
    result = None
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.x-rates.com/calculator/")
        wait = WebDriverWait(driver, 10)
        
        amount = wait.until(EC.presence_of_element_located((By.ID, "amount")))
        amount.clear()
        amount.send_keys(count)
        time.sleep(1)
        
        val1_html = driver.find_element(By.ID, "from")
        val1_html.click()  # Кликаем чтобы открыть список
        time.sleep(1)
        

        from_options = driver.find_elements(By.CSS_SELECTOR, "#from option")
        for option in from_options:
            if val_1 in option.text:
                option.click()
                break
        time.sleep(1)
        
        val2_html = driver.find_element(By.ID, "to")
        val2_html.click() 
        time.sleep(1)
        
        to_options = driver.find_elements(By.CSS_SELECTOR, "#to option")
        for option in to_options:
            if val_2 in option.text:
                option.click()
                break
        time.sleep(2)
        
        result_wait = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ccOutputRslt")))
        result = result_wait.text
        
    except Exception as e:
        print(f"Error: {e}")
        return e
    finally:
        driver.quit()
        return result

print(conv("EUR - Euro", "USD - US Dollar", "10"))
