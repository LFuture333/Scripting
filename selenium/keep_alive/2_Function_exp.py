from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver


def chromedriver_function(url):
    #Start Webdriver   
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=options)


    driver.get(url)

    return driver.page_source



def t1(driver):

    driver.get("http://www.google.com")

def t2(driver):
    driver.get("http://www.facebook.com")



driver = chromedriver_function("http://youtube.com")

t1(driver)

t2(driver)