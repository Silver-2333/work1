# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

import requests
import re
import time
def get_one_page(url,page):#请求函数：获取某一网页上的所有内容
    headers = {
    'User-agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Host' : 'weibo.cn',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Language' : 'zh-CN,zh;q=0.9',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Cookie' : '_T_WM=83369d47b52789af94bee540e8e94de1; __guid=78840338.3194298714216146000.1608960926792.6733; SCF=Ar_I8MBXKRAEmOx9xDNNP4ID63PVlmBXvLYI2vhK07RTJTGfHGYo6eD3iLUtj5okKWXJKH3rKbOhw6BgWfTE5e8.; SUB=_2A25y4pM3DeRhGeFL71MQ8CzPwjqIHXVuLD1_rDV6PUJbktANLRXwkW1NQg2GdE9wJpxDCtnGG2OApFnzIFXw386N; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhokEhV8iipC60B_hY7oRVS5NHD95QNSKBpeK5Ee0.cWs4Dqcj_i--ci-8hi-2Ei--Xi-z4iK.7i--fi-z7iKysi--ciK.NiKyFi--4i-20iKy8; SSOLoginState=1608967015; monitor_count=55',
    'DNT' : '1',
    'Connection' : 'keep-alive'
     }#请求头的书写，包括User-agent,Cookie等
    start_time = time_params_formatter('2020-05-31-04', offset_hour=-8)
    end_time = time_params_formatter('2020-06-10-05', offset_day=-1, offset_hour=-7)
    params = {
        'hideSearchFrame': '',
        'keyword': '疫情',
        'advancedfilter': '1',
        'starttime': start_time,
        'endtime': end_time,
        'sort': 'time',
        'page': page
    }
    response = requests.get(url,params=params,headers=headers, verify=False)  # 利用requests.get命令获取网页html
    if response.status_code == 200:  # 状态为200即为爬取成功
        return response.text  # 返回值为html文档，传入到解析函数当中
    return None


def time_params_formatter(params_time, offset_day=0, offset_hour=-8):
    [temp_year, temp_month, temp_day, temp_hour] = [int(e) for e in params_time.split('-')]
    print(temp_year)
    temp_date = datetime(year=temp_year, month=temp_month, day=temp_day, hour=temp_hour)
    temp_offset = timedelta(days=offset_day, hours=offset_hour)
    res_time = (temp_date + temp_offset).strftime('%Y-%m-%d-%H')
    return res_time

def parse_one_page(html):#解析html并存入到文档result.txt中
    pattern = re.compile('<span class="ctt">.*?</span>', re.S)
    items = re.findall(pattern,html)
    result = str(items)
    parse_one_page_plus(result)

num=1
def parse_one_page_plus(content):
    global num
    rawResults = re.findall(">.*?<", content, re.S)
    firstStepResults = []
    for result in rawResults:
        # print(result)
        if ">\'][\'<" in result:
            continue
        if ">:<" in result:
            continue
        if ">回复<" in result:
            continue
        if "><" in result:
            continue
        if ">\', \'<" in result:
            continue
        if "@" in result:
            continue
        if "> <" in result:
            continue
        else:
            firstStepResults.append(result)
    subTextHead = re.compile(">")
    subTextFoot = re.compile("<")
    ret = ""
    for lastResult in firstStepResults:
        resultExcel1 = re.sub(subTextHead, '', lastResult)
        resultExcel = re.sub(subTextFoot, '', resultExcel1)
        if not '#'in resultExcel and resultExcel !='疫情':
            print(num, resultExcel)
            ret = ret + "\n" + str(num) + " " + str(resultExcel)
            num += 1
    with open('第四阶段下.txt', 'a+', encoding='utf-8') as fp:
        fp.write(ret)

for i in range(40,100):
    url = "https://weibo.cn/search/mblog"
    html = get_one_page(url,i)
    print('正在爬取第 %d 页评论' % (i+1))
    parse_one_page(html)
    time.sleep(1)