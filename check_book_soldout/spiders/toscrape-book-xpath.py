# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-book-xpath'
    start_urls = [
        'https://search.kyobobook.co.kr/mobile/search?keyword=코스모폴리스',
    ]

    def parse(self, response):
        print('//*[@id="search_list_layout"]/li[1]/a[1]/div[2]/strong')
        for book in response.xpath('//*[@id="search_list_layout"]'):
            yield {
                'title': book.xpath('//*[@id="search_list_layout"]/li[1]/a[1]/div[2]/strong/text()').extract_first()
            }
            print(book.xpath('//*[@id="search_list_layout"]/li[1]/a[1]/div[2]/strong/text()').extract_first())

        #for quote in response.xpath('//div[@class="m-brick grid-item boxy bqQt"]'):
        #    yield {
        #        'text': quote.xpath('.//div/div[1]/div/a/text()').extract_first(),
        #        'author': quote.xpath('.//div/div[1]/div/div/a/text()').extract_first(),
        #        'tags': quote.xpath('.//div/div[1]/div/div/div/div/a[@class="qkw-btn btn btn-xs oncl_list_kc"]/text()').extract()
        #    }

# //*[@id="search_list_layout"]/li[2]/a[1]/div[2]/strong

# //*[@id="search_list_layout"]/li[2]/a[1]/div[2]/strong

