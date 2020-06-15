# -*- coding: utf-8 -*-

import pandas as pd

import MySQLdb
import pymysql
import re

if __name__ == '__main__':
    sql = "insert into jobinfo (JobName, ComName, Workplace, Salary, PubTime) VALUES (%s, %s,%s,%s,%s)"
    sql2 = "insert into jobinfo4 (name) VALUES (%s)"
    dict = {'ComName': '上海威士顿信息技术股份有限公司',
            'JobName': '大数据运维工程师',
            'PubTime': '06-15',
            'Salary': '0.8-1万/月',
            'Workplace': '合肥-包河区'}
    cxn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='bit1993',
        db='jobspider',
    )
    if '万/月' in dict['Salary']:
        salary_low = re.findall('(\d+\.?\d*)-', dict['Salary'])
        salary_high = re.findall('-(\d+\.?\d*)', dict['Salary'])
        print(salary_low[0])
        print(salary_high[0])
    else:
        print('no')

    # cur = cxn.cursor()
    # cur.execute(sql, (dict['JobName'], dict['ComName'], dict['Workplace'], dict['Salary'], dict['PubTime']))
    # # # cur.execute(sql, ('2',"地",'&','2','2'))
    # # name = '中文玩儿吖'
    # #
    # # cur.execute(sql2, name)
    #
    # # 连接MySQL，并提交数据
    # cxn.commit()
    # cxn.close()

    # # MySQL导入DataFrame
    # # 填写自己所需的SQL语句，可以是复杂的查询语句
    # sql_query = 'select * from user;'
    #
    # # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
    # df_read = pd.read_sql_query(sql_query, conn)
    # print(df_read)
    # conn.close()
