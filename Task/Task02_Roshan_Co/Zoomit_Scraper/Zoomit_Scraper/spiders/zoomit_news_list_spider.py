# import scrapy


# class ZoomitNewsListSpiderSpider(scrapy.Spider):
#     name = "zoomit_news_list"
#     allowed_domains = ["zoomit.ir"]
#     start_urls = ["https://www.zoomit.ir/search/news/"]

#     def parse(self, response):
#         All_News_List = response.xpath("//div[@class='sc-73a1c33f-0 cWbCJr']/a/span/text()").getall()
#         title_test_1 = response.xpath("//a/@href/text()").getall()
#         title_test_2 = response.xpath("//span/text()").getall()
#         title_test_3 = response.xpath("//span[@class='sc-63f15cb9-0 cbzARJ sc-1ff426ee-2 iEbDzs']/text()").getall()

#         yield{
#             "test1": All_News_List,
#             "test2": title_test_1,
#             "test3": title_test_2,
#             "test4": title_test_3
#         }

#------------------------------------------------------

# # import scrapy


# # class ZoomitNewsListSpiderSpider(scrapy.Spider):
# #     name = "zoomit_news_list"
# #     allowed_domains = ["zoomit.ir"]
# #     start_urls = ["https://www.zoomit.ir/search/news/"]

# #     def parse(self, response):
# #         All_News_List = response.xpath("//div[@class='sc-73a1c33f-0 cWbCJr']")

# #         for All_News in All_News_List:
# #             Title = All_News.xpath(".//a/span/text()").getall()
# #             # Content = All_News.xpath().getall()
# #             # Tags = All_News.xpath().getall()
# #             # Date_time = All_News.xpath().get()
# #             # Author = All_News.xpath().get()
# #             # Source = All_News.url

# #             yield{
# #                 "Title": Title
# #                 # "Content": Content,
# #                 # "Tags": Tags,
# #                 # "Date_time": Date_time,
# #                 # "Author": Author,
# #                 # "Source": Source
# #             }
            
#------------------------------------------------------

# #         # Source = response.url

# #         # yield{
# #         #     'Source': Source
# #         # }
