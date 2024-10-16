from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import scrapy


# option_1 = webdriver.ChromeOptions()
# service_1 = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service_1, options=option_1)

# driver.get("https://www.zoomit.ir/search/news/")
# time.sleep(3)

# print(driver.title)

class ZoomitSpiderSpider(scrapy.Spider):
    name = "Zoomit_Spider"
    allowed_domains = ["zoomit.ir"]
    #start_urls = ["https://zoomit.ir"]
    start_urls = ["https://www.zoomit.ir/search/news/"]

    
    def __init__(self, *args, **kwargs):
        super(ZoomitSpiderSpider, self).__init__(*args, **kwargs)
        self.option_1 = webdriver.ChromeOptions()
        self.service_1 = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service_1, options=self.option_1)

    def parse(self, response):
        self.driver.get(response.url)
        URL_Source_Driver = self.driver.current_url
        time.sleep(3)

        Page_Source = self.driver.page_source
        Selector_HTML = scrapy.Selector(text=Page_Source)
        All_News_Search = Selector_HTML.xpath("//*[@id='__next']/div[2]/div[1]/div[4]/div/div/div/div/ul")
                                        # /html/body/div/div[2]/div[1]/div[4]/div/div/div/div/ul/li[2]/div/div/div/div/a/span
                                        # //*[@id="__next"]/div[2]/div[1]/div[4]/div/div/div/div/ul/li[2]/div/div/div/div/a/span    
        for News_Search in All_News_Search:
            #Title = News_Search.xpath(".//span/text()").getall()
            Title = ''.join(News_Search.xpath(".//a/span/text()").getall()).strip()
            Date = ''.join(News_Search.xpath(".//span[1]/span").getall()).strip()
            Study_Time = ''.join(News_Search.xpath(".//span[2]").getall()).strip()


        yield{
            "Title": Title,
            "Date" : Date,
            "Study Time": Study_Time,
            "URL Source Driver": URL_Source_Driver
        }

        # Next_Page = response.xpath("//a[contains(text(),'Next')]/@href").get()
        # if Next_Page:
        #     yield response.follow(Next_Page, self.parse)

        
    # def close(self):
    #     self.driver.quit()

#driver.quit()


# --------------------------------------------------------------------------------------------------------------------------------


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# import time
# import scrapy

# # option_1 = webdriver.ChromeOptions()
# # service_1 = Service(ChromeDriverManager().install())
# # driver = webdriver.Chrome(service=service_1, options=option_1)

# # driver.get("https://www.zoomit.ir/search/news/")
# # time.sleep(3)

# # print(driver.title)

# class ZoomitSpiderSpider(scrapy.Spider):
#     name = "Zoomit_Spider"
#     allowed_domains = ["zoomit.ir"]
#     #start_urls = ["https://zoomit.ir"]
#     start_urls = ["https://www.zoomit.ir/search/news/"]


#     def __init__(self, *args, **kwargs):
#         super(ZoomitSpiderSpider, self).__init__(*args, **kwargs)
#         self.option_1 = webdriver.ChromeOptions()
#         self.service_1 = Service(ChromeDriverManager().install())
#         self.driver = webdriver.Chrome(service=self.service_1, options=self.option_1)

#     def parse(self, response):
#         self.driver.get(response.url)
#         URL_Source_Driver = self.driver.current_url
#         time.sleep(3)

#         Page_Source = self.driver.page_source
#         Selector_HTML = scrapy.Selector(text=Page_Source)
#         All_News_Search = Selector_HTML.xpath("//*[@id='__next']/div[2]/div[1]/div[4]/div/div/div/div/ul")
#                                         # /html/body/div/div[2]/div[1]/div[4]/div/div/div/div/ul/li[2]/div/div/div/div/a/span
#                                         # //*[@id="__next"]/div[2]/div[1]/div[4]/div/div/div/div/ul/li[2]/div/div/div/div/a/span    
#         for News_Search in All_News_Search:
#             #Title = News_Search.xpath(".//span/text()").getall()
#             Title = ''.join(News_Search.xpath(".//a/span/text()").getall()).strip()
#             Date = ''.join(News_Search.xpath(".//span[1]/span").getall()).strip()
#             Study_Time = ''.join(News_Search.xpath(".//span[2]").getall()).strip()


#         yield{
#             "Title": Title,
#             "Date" : Date,
#             "Study Time": Study_Time,
#             "URL Source Driver": URL_Source_Driver
#         }


#     # def close(self):
#     #     self.driver.quit()

# #driver.quit()



# --------------------------------------------------------------------------------------------------------------------------------

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service

# option_1 = webdriver.ChromeOptions()
# service_1 = Service(ChromeDriverManager().install())

# #driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome(service=service_1, options=option_1)

# driver.get("https://zoomit.ir")

# print(driver.title)

# driver.quit()

# --------------------------------------------------------------------------------------------------------------------------------

# import scrapy


# class ZoomitSpiderSpider(scrapy.Spider):
#     name = "Zoomit_Spider"
#     allowed_domains = ["zoomit.ir"]
#     #start_urls = ["https://zoomit.ir"]
#     start_urls = ["https://www.zoomit.ir/search/news/"]

#     def parse(self, response):
#         All_News_Search = response.xpath("//span").extract()

#         yield{
#             "test1": All_News_Search
#         }

#         # Source = response.url

#         # yield{
#         #     "Source": Source
#         # }
