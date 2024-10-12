import scrapy

class ZoomitNewsSpider(scrapy.Spider):
    name = "zoomit_news"
    start_urls = ["https://www.zoomit.ir/featured-articles/427723-len-sassaman-satoshi-nakamoto-bitcoin/"]

    def parse(self, response):

        title = response.css('h1.sc-63f15cb9-0.eDUhpq::text').get()
        content = response.css('div.sc-73a1c33f-0.Iywl div.sc-b3350405-0.ekZGug div.sc-b3350405-1.ghrpOF p.sc-63f15cb9-0.chyqyp.sc-4bdf9365-0.brkdqE::text').getall()
        tags = response.css('div.header-detail a.sc-f3acbc5d-0 span.sc-63f15cb9-0.dDbOrc::text').getall()
        date_time = response.css('span.fa::text').get()
        author = response.css('span.sc-63f15cb9-0.fFMZDJ::text').get()
        source = response.url

        yield {
            'title': title,
            'tags': tags,
            'date_time': date_time,
            'author': author,
            'source': source,
            'content': content,
        }
