import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from scrapy.spiders import Spider
from JobSpider.items import JobspiderItem
from scrapy.selector import Selector

import json


# class JobSpider(RedisSpider):
class JobSpider(Spider):
    name = "jobSpider"
    host = "https://www.51job.com/"
    # redis_key = "jobSpider:start_urls"

    start_urls = [

    ]
    url = 'https://sou.zhaopin.com/?jl=665&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&kt=3'

    def start_requests(self):
        yield Request(url=self.url, callback=self.joblist_parse)




    def joblist_parse(self, response):
        f = open('job.html', 'wb')
        f.write(response.body)
        f.close()

        selector = Selector(response)
        job_list = selector.xpath('//div[@id="listContent"]')
        for job in job_list:
            # job_primary = job_list.xpath('//div[@class="job-primary"]')
            job_detail_url = job_list.xpath(('//a/@href')).get()
            print(job_detail_url)

# url_next = selector.xpath(
#     u'body//div[@class="pa" and @id="pagelist"]/form/div/a[text()="\u4e0b\u9875"]/@href'  # 下一页
# ).get()
