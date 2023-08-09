import threading
from selenium import webdriver
import time


class ScrapeThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
       
        page_source = driver.page_source
        input("test continue")
        driver.close

urls = [
    'https://en.wikipedia.org/wiki/0',
    'https://en.wikipedia.org/wiki/1',
    'https://en.wikipedia.org/wiki/2',
    'https://en.wikipedia.org/wiki/3',
]

threads = []
for url in urls:
    t = ScrapeThread(url)
    
    t.start()
    threads.append(t)

for t in threads:
    t.join()