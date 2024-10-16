from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json

options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.reuters.com/site-search/?query=Commodity+Gold') 


cookies = driver.get_cookies()

for cookie in cookies:
    print(cookie)


with open('cookies.json', 'w') as file:
    json.dump(cookies, file, indent=4)

driver.quit()




