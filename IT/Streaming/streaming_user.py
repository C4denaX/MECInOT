from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from time import sleep
def set_chrome_options():
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    return chrome_options

if __name__ == "__main__":
    chrome_options = set_chrome_options()
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get("http://10.0.0.7")
    print(driver.title)
    try:
        while True:
            driver.find_element(By.ID,"videoPlayer").click()
            sleep(20)
            driver.refresh()
            print("Page reloaded")
    except:
        driver.close()
        os._exit(0)

