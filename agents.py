import scrapy
# from scrapy import Spider, Request
from ..items import DataExtractionItem

class agentsSpider(scrapy.Spider):
    name = 'details_extraction'
    # page_number = 2
    start_urls = ['https://www.bhhsamb.com/agents/']

    def parse(self, response):
        agents = response.xpath("//div[@class = 'col-md-8 col-sm-12']")
        max_page = 43
        next_page = response.xpath("//li[@class = 'page-item next']/a/@href").get()
        for i in range(1, max_page+1):
            for agent in agents:
                yield response.follow(url = agent.xpath(".//span/a/@href").get(),callback = self.parse_agents)
            if i <= 43:
                yield response.follow(next_page, callback = self.parse)
    def parse_agents(self, response):
        item = DataExtractionItem()
        # for data in response.xpath("//div[@class = 'col-sm-24 kill padding']"):
        name = response.xpath("//div[@class = 'row']/h1[@class = 'body-title']/text()").extract()
        job_title = response.xpath("////span[@class = 'big-text']/text()")[0].extract()
        image_url = response.xpath("//img[@class = 'agent-photo']/@src").extract()
        address = response.xpath("//div[@class='text-left medium-text mobile-text-center']/text()").extract()
        contact_details = response.xpath("/html/body/div[5]/div/div/div[1]/div/div[4]/div/div[1]/div/div/a[1]/text()").extract()
        social_accounts = response.xpath("//div[@class = 'agent-social-icons social']/a[@class = 'fb']/@href").extract()
        offices = response.xpath("/html/body/div[5]/div/div/div[1]/div/div[5]/div/div/div[1]/a/text()").extract()
        languages = response.xpath("/html/body/div[5]/div/div/div[1]/div/div[5]/div/div/div[3]/ul/li/text()").extract()
        description = response.xpath("/html/body/div[5]/div/div/div[1]/div/div[8]/div[2]/div/p[1]/text()").extract()
            # description2 = response.xpath("/html/body/div[5]/div/div/div[1]/div/div[8]/div[2]/div/p[2]/text()").extract()
            # description3 = response.xpath("/html/body/div[5]/div/div/div[1]/div/div[8]/div[2]/div/p[3]/text()").extract()

        item['Name'] = name
        item['Job_title'] = job_title
        item['Image_url'] = image_url
        item['Address'] = address
        item['Contact_details'] = contact_details
        item['Social_accounts'] = social_accounts
        item['Offices'] = offices
        item['Languages'] = languages
        item['Description'] = description
       

        yield item
