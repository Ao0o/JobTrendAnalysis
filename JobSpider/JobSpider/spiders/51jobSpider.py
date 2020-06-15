import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from scrapy.spiders import Spider
from JobSpider.items import JobspiderItem
from scrapy.selector import Selector
from scrapy_splash import SplashRequest

import re

import json


# class JobSpider(RedisSpider):
class JobSpider(Spider):
    name = "jobSpider"
    host = "https://www.51job.com/"
    # redis_key = "jobSpider:start_urls"

    start_urls = [

    ]
    # 合肥，大数据
    url = 'https://search.51job.com/list/150200,000000,0000,00,9,99,%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

    def start_requests(self):
        yield Request(url=self.url, callback=self.joblist_parse)

    def joblist_parse(self, response):
        selector = Selector(response)
        job_item = JobspiderItem()
        job_list = selector.xpath('//div[@class="el"]')

        for job in job_list:
            # job_primary = job_list.xpath('//div[@class="job-primary"]')
            job_detail_url = job.xpath('p/span/a/@href').get()
            job_name = job.xpath('p/span/a/@title').get()
            com_name = job.xpath('span[@class="t2"]/a/text()').get()
            work_place = job.xpath('span[@class="t3"]/text()').get()
            salary = job.xpath('span[@class="t4"]/text()').get()
            pub_time = job.xpath('span[@class="t5"]/text()').get()
            if job_name:
                job_item['JobName'] = job_name
            if com_name:
                job_item['ComName'] = com_name
            if work_place:
                job_item['Workplace'] = work_place
            if salary:
                if '千/月' in salary:
                    salary_low = re.findall('(\d+\.?\d*)-', salary)
                    salary_low = float(salary_low[0]) *1000
                    salary_high = re.findall('-(\d+\.?\d*)', salary)
                    salary_high = float(salary_high[0]) * 1000
                elif '万/月' in salary:
                    salary_low = re.findall('(\d+\.?\d*)-', salary)
                    salary_low = float(salary_low[0]) *10000
                    salary_high = re.findall('-(\d+\.?\d*)', salary)
                    salary_high = float(salary_high[0]) *10000
                elif '万/年' in salary:
                    salary_low = re.findall('(\d+\.?\d*)-', salary)
                    salary_low = float(salary_low[0]) * 10000 / 12
                    salary_high = re.findall('-(\d+\.?\d*)', salary)
                    salary_high = float(salary_high[0]) * 10000 / 12
                else:
                    print("unknown salary")
                job_item['SalaryLow'] = salary_low
                job_item['SalaryHigh'] = salary_high
            if pub_time:
                job_item['PubTime'] = pub_time

            yield job_item

        ###################
        # if job_detail_url:
        #     yield Request(url=job_detail_url, callback=self.job_detail_parse)

        url_next = selector.xpath(
            u'body//div[@class="p_in"]/ul/li/a[text()="\u4e0b\u4e00\u9875"]/@href'
            # get next page url
        ).get()
        if url_next:
            yield Request(url=url_next, callback=self.joblist_parse)

    def job_detail_parse(self, response):
        selector = Selector(response)
        job_item = JobspiderItem()
        detail_info = selector.xpath('//div[@class="tCompanyPage"]')
        # job_item['JobName'] = detail_info.xpath('//h1/@title').get()
        # job_item['ComName'] = detail_info.xpath('//p[@class="cname"]/a/@title').get()
        msgs = detail_info.xpath('//p[@class="msg ltype"]/text()').getall()
        for msg in msgs:
            msg = "".join(msg.split())

        print(job_item)

        # Welfare = Field()
        # WorkExp = Field()
        # Education = Field()
        # RecruitNum = Field()
        # JobResp = Field()  # Job responsibility
        # JobReq = Field()  # Job requirement
        # SkillReq = Field()  # Skill requirement
        # DetailLoc = Field()  # Detail location

# url_next = selector.xpath(
#     u'body//div[@class="pa" and @id="pagelist"]/form/div/a[text()="\u4e0b\u9875"]/@href'  # 下一页
# ).get()
