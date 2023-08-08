# import module
from selenium import webdriver
  
# Create object
driver = webdriver.Chrome()
  
# Assign URL
url = "https://www.geeksforgeeks.org/"
  
# New Url
new_url = "https://www.facebook.com/"
  
# Opening first url
driver.get(url)
  
# Open a new window
driver.execute_script("window.open('');")
  
# Switch to the new window and open new URL
driver.switch_to.window(driver.window_handles[1])
driver.get(new_url)

input(" AWAIT")