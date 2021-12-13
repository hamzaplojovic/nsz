import scrapy


class NszSpider(scrapy.Spider):
    name = 'nsz'
    allowed_domains = ['www.nsz.gov.rs']
    start_urls = ['http://http://www.nsz.gov.rs/employee/jobs/search?page=1/',
                  'http://http://www.nsz.gov.rs/employee/jobs/search?page=2/']

    def parse(self, response):
        for job in response.css('div.single-job'):
            job.xpath('div[1]/@onclick').get()
            pass