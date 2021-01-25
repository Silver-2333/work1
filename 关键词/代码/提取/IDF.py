# -*- coding:utf-8 -*-
from pyhanlp import *
import math
document = open("D:/ADocuments/My homework/数据科学/开始了/3月下.txt",encoding="utf-8").read()
document+=open("D:/ADocuments/My homework/数据科学/开始了/4月上.txt",encoding="utf-8").read()
document+=open("D:/ADocuments/My homework/数据科学/开始了/4月下.txt",encoding="utf-8").read()
document+=open("D:/ADocuments/My homework/数据科学/开始了/5月上.txt",encoding="utf-8").read()
document+=open("D:/ADocuments/My homework/数据科学/开始了/5月上.txt",encoding="utf-8").read()
document+=open("D:/ADocuments/My homework/数据科学/开始了/5月下.txt",encoding="utf-8").read()
document+=open("D:/ADocuments/My homework/数据科学/开始了/6月上.txt",encoding="utf-8").read()
document+=open("D:/ADocuments/My homework/数据科学/开始了/6月下.txt",encoding="utf-8").read()
list=document.split("1 :")
N=len(list)
list=open("最终关键字/关键词四阶段TF处理.txt",encoding="utf-8").read().split()
print(list)
keyword_list = []
for i in range(0,300,3):
    keyword_list.append(str(list[i]))
print(keyword_list)
dict = {};
with open('四阶段IDF2.txt', 'a+', encoding='utf-8') as fp:
    fp.write(str(N))
    fp.write("\n")
for item in keyword_list:
    count=1
    for i in list:
        if item in i:
            count=count+1
    dict[item]=math.log(N/count)
dict=sorted(dict.items(), key = lambda kv:(kv[1], kv[0]))

for item in dict:

    with open('四阶段IDF2.txt', 'a+', encoding='utf-8') as fp:
        fp.write(item[0]+"   ")
        fp.write(str(item[1])+"   ")
        fp.write(str(item[1]*1000))
        fp.write("\n")