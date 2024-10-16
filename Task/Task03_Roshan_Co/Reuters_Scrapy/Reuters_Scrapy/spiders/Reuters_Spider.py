from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import json

class ReutersScraper:
    def __init__(self):
        self.option_1 = webdriver.ChromeOptions()
        self.option_1.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36")
        self.service_1 = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service_1, options=self.option_1)

    def list_cookies(self):
        with open("cookies.json", 'r') as Cookies_File:
            Cookies_Reuters = json.load(Cookies_File)

        for Cookie_Reuters in Cookies_Reuters:
            self.driver.add_cookie(Cookie_Reuters)
        # Cookies_Reuters = []
        # Read_All_Cookies = self.driver.get_cookies()
        
        # for Read_Cookies in Read_All_Cookies:
        #     Cookies_Reuters.append(Read_Cookies)
        #     print(Read_Cookies, "\n")
        

        # for Cookie_Reuters in Cookies_Reuters:
        #     self.driver.add_cookie(Cookie_Reuters)
        #     print(Cookie_Reuters)

        
    def get_page_data(self):
        self.driver.get("https://www.reuters.com/site-search/?query=Commodity+Gold")
        time.sleep(3) 

        self.list_cookies()
        time.sleep(3) 
        
        self.driver.refresh() 
        time.sleep(3) 


        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "title")))
            Page_Title = self.driver.title
            Url_Source_Driver = self.driver.current_url

            All_News_Title = self.driver.find_elements(By.CLASS_NAME, 'text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_6__1qUJ5 heading__base__2T28j heading__heading_6__RtD9P')
            News_Titles = [News.text for News in All_News_Title]


            with open('Reuters_Data_Search_Gold.csv', 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["URL", "Title", "Articles"])
                csv_writer.writerow([Url_Source_Driver, Page_Title, ', '.join(News_Titles)])

        except Exception as err:
            print(f"Error: {err}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    scraper = ReutersScraper()
    scraper.get_page_data()
