import scrapy
from bilibili_api import video
from ..items import BilibiliListScrItem
import time

class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['https://www.bilibili.com/v/popular/rank/all']

    def parse(self, response):
        items = BilibiliListScrItem()
        lists = response.xpath('//div[@id="app"]/div[2]/div[2]/ul/li')
        for i in lists:
            items['date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            items['type'] = 'all'
            items['rank'] = i.xpath('./div[1]/text()').get()
            items['url'] = i.xpath('./div[2]/div[1]/a/@href').get()[2:]
            # items['pic'] = i.xpath('./div[2]/div[1]/a/img/@data-src').get()
            items['name'] = i.xpath('./div[2]/div[2]/a/text()').get()
            items['bv'] = i.xpath('./div[2]/div[1]/a/@href').get()[25:]
            v = video.get_video_info(bvid=items['bv'])
            items['pic'] = v['pic']
            items['aid'] = v['aid']
            items['view'] = v['stat']['view']
            items['up'] = v['owner']['name']
            items['upId'] = v['owner']['mid']
            yield items
