import scrapy


class NzsCrawlerSpider(scrapy.Spider):
    name = 'nzs_crawler'
    allowed_domains = ['http://www.nsz.gov.rs/live/trazite-posao/poslovi-oglasi?sid=Novi+Pazar&ctid=']
    start_urls = ['http://www.nsz.gov.rs/live/trazite-posao/poslovi-oglasi?sid=Novi+Pazar&ctid=']

    def parse(self, response):
        with open('index.txt', 'w') as f:
            data = str(response.xpath('/html/body/div[1]/div/div/div[3]/div[1]/div[1]/div[2]/div/div/div').extract())
            data = str(data[2:-2])
            f.write(data)
        with open("index.txt") as f:
            lines = f.readlines()
            stocks = [x.replace("\r\n","") for x in lines]
            f.write(stocks)
