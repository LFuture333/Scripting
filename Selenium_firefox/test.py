from selenium import webdriver
from selenium.webdriver.firefox.service import Service

firefox_services = Service(executable_path='firefoxdriver', port=3000, service_args=['--marionette-port', '2828', '--connect-existing'])
driver = webdriver.Firefox(service=firefox_services)
driver.get('https://youtube.com')
driver.execute_script('alert(\'your favorite music is here\')')