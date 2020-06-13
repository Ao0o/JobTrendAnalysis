import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request


class JobSpider(RedisSpider):
    name = "jobSpider"
    host = "http://51job.com"
    redis_key = "jobSpider:start_urls"

    start_urls = [

    ]

    def start_requests(self):
        pass

    def job_parse(self, response):
        pass
