# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    JobName = Field()
    ComName = Field()  # Company Name
    SalaryLow = Field()
    SalaryHigh = Field()
    Welfare = Field()
    Workplace = Field()
    WorkExp = Field()
    Education = Field()
    RecruitNum = Field()
    PubTime = Field()
    JobResp = Field()  # Job responsibility
    JobReq = Field()  # Job requirement
    SkillReq = Field()  # Skill requirement
    DetailLoc = Field()  # Detail location

class JoblistItem(scrapy.Item):
    URL = Field()