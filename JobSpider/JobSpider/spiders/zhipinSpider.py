import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from scrapy.spiders import Spider
from JobSpider.items import JobspiderItem
from scrapy.selector import Selector


# class JobSpider(RedisSpider):
class JobSpider(Spider):
    name = "zhipinSpider"
    host = "https://www.zhipin.com/"
    # redis_key = "jobSpider:start_urls"

    start_urls = [

    ]
    query = "c101220100/?query=%E5%A4%A7%E6%95%B0%E6%8D%AE"

    def start_requests(self):
        yield Request(url=self.host + self.query, callback=self.joblist_parse)

    def joblist_parse(self, response):
        selector = Selector(response)
        job_list = selector.xpath('//div[@class="job-list"]')
        for job in job_list:
            job_primary = job_list.xpath('//div[@class="job-primary"]')
            job_detail_url = job_primary.xpath(('//div[@class="primary-box"]/@href')).get()
            print(job_detail_url)

# url_next = selector.xpath(
#     u'body//div[@class="pa" and @id="pagelist"]/form/div/a[text()="\u4e0b\u9875"]/@href'  # 下一页
# ).get()
