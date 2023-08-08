import os

from selenium import webdriver


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Function handless the await for action (browser driver await)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_stealth import stealth


import time
import json


#####################################################################################
#####################################################################################
#Creating the stealth google tab
def Start_browser(headless):
    options = Options()
    options.add_argument("start-maximized")
    
    #if the headless parameter equal true 
    if (headless == True):

        #Then define the selenium as headless
        options.add_argument('--headless')

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    #This parameter are use to avoid the bot from being detected 
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)


    browser = webdriver.Chrome(options=options)

    #Selenium stealth setting 

    # Communicating to the web server that this user is a windows maching 
    stealth(browser,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
    )
    return browser

#Log in to the select user account 
def LogIn_Fidelity(browser,username, password):
    #Go  to link to beging log in process
    browser.get("https://oltx.fidelity.com/ftgw/fbc/oftop/portfolio#summary/")
    while True:
        #Detect the  username input in the website  
        wait = WebDriverWait(browser, 8)

        #wait for username input to be  available
        wait_username = wait.until(EC.element_to_be_clickable((By.ID, 'Login')) )

        #Wait for the password input to be available
        wait_password = wait.until(EC.element_to_be_clickable((By.ID, 'password')))

        #Wait for the log-in btn to be available to be click
        wait_Login = wait.until(EC.element_to_be_clickable((By.ID, 'fs-login-button')))

        #Find the usename input box by id
        userBox = browser.find_element(by='id', value='userId-input')

        #Find the password input box by id
        passBox = browser.find_element(by='id', value='password')

        #Find the login  button
        login_btn = browser.find_element(by='id', value='fs-login-button')


        #Enter the username to the input  box 
        userBox.send_keys(username)

        #Enter the password to the input box 
        passBox.send_keys(password)
    
        #Click the log-in button
        login_btn.click()

        time.sleep(5)    
 
        if (browser.find_element(By.CLASS_NAME, 'account-selector--all-accounts-balance')):
            print("Log In Successfull")
            break
    
    input("TT")
    browser.get('https://oltx.fidelity.com/ftgw/fbc/oftop/portfolio#summary/')

    All_Balance = browser.find_element(By.CLASS_NAME, 'account-selector--all-accounts-balance').text
    

    print("Log in successfully")
    print(str(All_Balance))


username = "Comp39443132313"
password = "Laptop1996Lw"


browser = Start_browser(False)
LogIn_Fidelity(browser, username, password)
