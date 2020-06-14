import requests  # 用于发送URL请求
# import pandas as pd # 用于构造数据框
import random  # 用于产生随机数
import time  # 用于时间停留#

url = r'https://fe-api.zhaopin.com/c/i/sou?_v=0.92155844&x-zp-page-request-id=b27d8047ba344991af83d787ceb6ef91-1592103374876-974510&x-zp-client-id=7bf03f53-4ab5-4bf1-d5a5-8924bb76471d&MmEwMD=5GBI3mN9oFLE7ypvQtce2mLUjIV_FVFGsOLPGaU.dEyINB73JuBPK1sA.mQ5SJplYKJpidA9reD2M1Ztso60HJpXH6VslIh5_dVnypu5CKHsKXCXFOcSmKD5tNpBjje7Wiaoh_p9i4LCL4pNUcnE8WPuK42cqZ3PORFopqzKleeOL8pG7iG4qPS1u9VzOPcVwob237CAstW6sek6EtqXaG3xSIkIcCqDo_QQWIyMLZzAFqu9wveKogHqJ.c4rHuB3nh5wNoAAvGX0Wi.2U80q7gF5XBk7gbReaYY2DQVNaWfobYM9XUdFzPH8I8qY4GkCX2qDQwSTlnD5lgYL5fYv7xq7P8sDN6.VdCIX5PL_bnxAoQrePDHIHkjgCp3L.IMGTB3sdoz3dp1LO9.PfKiJDL8_'
# 构造请求的头信息，防止反爬虫
headers = {    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# 利用requests包中的get函数发送请求
response = requests.get(url, headers = headers)
# 基于response返回Json数据
datas = response.json()


# if __name__ == '__main__':
#     spider = siper()
#     # cityname = input("请输入你要查询的城市的名称（市级城市）：")
#     # city = spider.get_citycode(cityname)
#     url = r'https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId=489&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&lastUrlQuery=%7B%22jl%22:%22489%22,%22kw%22:%22%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88%22,%22kt%22:%223%22%7D&at=9c5682b1a4f54de89c899fb7efc7e359&rt=54eaf1be1b8845c089439d53365ea5dd&_v=0.84300214&x-zp-page-request-id=280f6d80d733447fbebafab7b8158873-1541403039080-617179'
#     items = spider.parse_data(url)
