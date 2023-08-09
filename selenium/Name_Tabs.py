# import module
from selenium import webdriver


#create object 
driver = webdriver.Chrome()



driver.get('http://www.google.com')



#Second tab creation

#Open in a new browser tab
driver.execute_script("window.open('about:blank','2tab');")

#switch to tab 3 
driver.switch_to.window("2tab")
driver.get('http://www.facebook.com')


driver.execute_script("window.open('about:blank', '3tab');")
#switch to the second tab  
driver.switch_to.window("3tab")
driver.get('http://www.amazon.com')

while driver
   test = input( " DOne PRogram")
   print("TEST")