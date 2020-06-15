# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import MySQLdb
import pymysql

from JobSpider.items import JobspiderItem


class JobspiderPipeline:

    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='bit1993',
            db='jobspider',
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        sqli = "insert into jobinfo (JobName, ComName, Workplace, SalaryLow, SalaryHigh, PubTime) VALUES (%s, %s,%s,%s,%s, %s)"

        if isinstance(item, JobspiderItem):
            try:
                self.cur.execute(sqli,(item['JobName'], item['ComName'], item['Workplace'], item['SalaryLow'], item['SalaryHigh'], item['PubTime']))
                self.conn.commit()
            except Exception:
                pass
        # elif isinstance(item, TweetsItem):
        #     try:
        #         self.db[self.Tweetdb].insert_one(dict(item))
        #     except Exception:
        #         pass

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
