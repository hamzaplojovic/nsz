import scrapy


class NszSpider(scrapy.Spider):
    name = 'nsz'
    allowed_domains = ['www.nsz.gov.rs']
    start_urls = ['http://www.nsz.gov.rs/employee/jobs/search?page=1/',
                  'http://www.nsz.gov.rs/employee/jobs/search?page=2/']

    def parse(self, response):
        with open("data.html", "w") as f:
            f.write(str(response.selector.xpath('/html/body/main/section/div/div/div/div').get().split()))

        