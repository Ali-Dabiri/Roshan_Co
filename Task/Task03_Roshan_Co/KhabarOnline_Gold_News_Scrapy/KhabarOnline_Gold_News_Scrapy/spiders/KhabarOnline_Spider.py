import scrapy
from datetime import datetime, timedelta

class GoldNewsSpider(scrapy.Spider):
    name = "khabaronline_Gold_News"
    allowed_domains = ["khabaronline.ir"]
    start_urls = ["https://english.khabaronline.ir/search?a=0&q=gold&dr=all&df=&dt=&sort=date&pageSize=20"]

    def parse(self, response):
        All_News_Gold = response.xpath("//div[@class='desc']")
        Six_Months_Ago = datetime.now() - timedelta(days=180)

        
        
        for News_Gold in All_News_Gold:
            Title = ''.join(News_Gold.xpath(".//h3/a//text()").getall()).strip()
            News_Text = ''.join(News_Gold.xpath(".//p/text()").getall()).strip()
            # Tags_Parts = News_Gold.xpath(".//a[contains(@class, 'tag')]/text()").getall()
            # Tags = ', '.join(Tags_Parts)
            Source = response.url
            #Author = News_Gold.xpath(".//span[@class='author']/text()").get()
            Date_Time = News_Gold.xpath(".//time/a/text()").get()
            if Date_Time:
                Date_Time_Compare = datetime.strptime(Date_Time, "%d %B %y - %H:%M")
                if Date_Time_Compare >= Six_Months_Ago:
                    yield {
                        'Title': Title,
                        'News Text': News_Text,
                        #'Tags': Tags,
                        'Source': Source,
                        #'Author': Author,
                        'Publication Time': Date_Time
                    }

        Next_Page = response.xpath("//a[contains(text(),'Next')]/@href").get()
        if Next_Page:
            yield response.follow(Next_Page, self.parse)
