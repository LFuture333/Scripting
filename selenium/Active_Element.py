from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Function handless the await for action (browser driver await)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




options = Options()
options.add_argument("start-maximized")
    
    #if the headless parameter equal true 

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

    #This parameter are use to avoid the bot from being detected 
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)


driver = webdriver.Chrome()


driver.get("https://www.google.com")
driver.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("webElement")

    # Get attribute of current active element
attr = driver.switch_to.active_element.get_attribute("title")
print(attr)
  
