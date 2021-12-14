import scrapy
from bs4 import BeautifulSoup


class NszSpider(scrapy.Spider):
    name = 'nsz'
    allowed_domains = ['www.nsz.gov.rs']
    start_urls = ['http://www.nsz.gov.rs/employee/jobs/search?page=1/',
                  'http://www.nsz.gov.rs/employee/jobs/search?page=2/']

    def parse(self, response):
        item = str(response.selector.xpath('/html/body/main/section/div/div/div/div').get())
        with open("data.html", 'w') as w:
            w.write(str(item))
        with open("data.html", 'w') as f:
            soup = BeautifulSoup(open("data.html"))
            for tag in soup.find_all('p'):
                f.write("<div>"+tag+"</div>")

        