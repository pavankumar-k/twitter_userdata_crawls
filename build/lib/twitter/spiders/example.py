# -*- coding: utf-8 -*-
import scrapy
import pkgutil

class ExampleSpider(scrapy.Spider):
    name = 'example'
    def start_requests(self):
        urls = self.getUrls()
        self.log(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def getUrls(self):
        addurls = []
        data = pkgutil.get_data("twitter", "resources/links.txt")
        addurls = (data.decode('utf-8')).split('\n')
        url = [(s.strip()).replace(',','') for s in addurls]
        self.log('Total urls:'+str(len(url)))
        return url

    def parse(self, response):
        yield{
            'f1':response.request.url,
            'f2':(' '.join([x.strip() for x in response.css('h1.ProfileHeaderCard-name *::text').extract()])).strip(),
            'f3':(' '.join([x.strip() for x in response.css('h2.ProfileHeaderCard-screenname.u-inlineBlock.u-dir *::text').extract()])).strip(),
            'f4':'; '.join(response.css('p.ProfileHeaderCard-bio.u-dir *::text').extract())
            }
