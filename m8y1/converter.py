from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def conv(val_1,val_2,count):
    result = None
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.x-rates.com/calculator/")
        wait = WebDriverWait(driver,2)
        #amount = wait.until(EC.presence_of_element_located((By.ID,"amount")))
        #amount.clear()
        time.sleep(5)
        amount = driver.find_element(By.ID,"amount")
        time.sleep(2)
        amount.send_keys(count)
        time.sleep(2)
        val1_html = driver.find_element(By.ID,"from")
        print(1)
        val1_html.send_keys(val_1)
        print(2)
        time.sleep(2)
        val2_html = driver.find_element(By.ID,"to")
        val2_html.send_keys(val_2)
        time.sleep(2)
        result_wait = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"ccOutputRslt")))
        result = result_wait.text
    except Exception as e:
        return e
    finally:

        driver.quit()
        return result
print(conv("EUR - Euro","USD - US Dollar","10"))
