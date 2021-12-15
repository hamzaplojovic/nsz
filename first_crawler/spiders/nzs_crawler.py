import scrapy
from bs4 import BeautifulSoup
import json

class NszSpider(scrapy.Spider):
    name = 'nsz'
    allowed_domains = ['www.nsz.gov.rs']
    start_urls = ['http://www.nsz.gov.rs/employee/jobs/search?page=1/',
                  'http://www.nsz.gov.rs/employee/jobs/search?page=2/']

    def parse(self, response):
        # with open("data.html", "w") as f:
        #     f.write(str(response.selector.xpath('/html/body/main/section/div/div/div/div').get().split()))
        with open("data2.json", 'w') as f:
            soup = BeautifulSoup(open("data.html"))
            divs = soup.find_all('h3')
            h3 = {}
            h3["h"] = str(divs)
            f.write(str(h3))
        

        