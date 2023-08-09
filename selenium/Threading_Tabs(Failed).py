import threading
from selenium import webdriver
import time

class ScrapeThread(threading.Thread):
    def __init__(self, url, tabs_count):
        threading.Thread.__init__(self)
        self.url = url
        self.tabs_count = tabs_count

    def run(self):
        driver = webdriver.Chrome()
        

        #Create the tabs here
        driver.execute_script("window.open('');")

        #Switch to the new tab
        driver.switch_to.window(driver.window_handles[self.tabs_count])


        driver.get(self.url)



        page_source = driver.page_source
        input("Continue test")

        


urls = [
    'https://en.wikipedia.org/wiki/0',
    'https://en.wikipedia.org/wiki/1',
    'https://en.wikipedia.org/wiki/2',
    'https://en.wikipedia.org/wiki/3',
]

threads = []
tabs_count= 0
for url in urls:
    
    t = ScrapeThread(url, tabs_count)
    
    tabs_count + tabs_count + 1
    t.start()
    threads.append(t)

for t in threads:
    t.join()