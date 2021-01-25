# -*- coding:utf-8 -*-
from pyhanlp import *

document = open("D:/ADocuments/My homework/数据科学/开始了/12月.txt",encoding="utf-8").read()
document+=open("D:/ADocuments/My homework/数据科学/开始了/1月上.txt",encoding="utf-8").read()

HanLP.Config.ShowTermNature = False
list=HanLP.segment(document)
list1=open("一阶段分词.txt",encoding="utf-8").read().split()
print(list1)

for i in list:
    if not i in list1:
        list1.append(i)
        print(i)
dict = {}
for item in list1:
    count = document.count(str(item))
    dict[item] = count

dict=sorted(dict.items(), key = lambda kv:(kv[1], kv[0]),reverse = True)

for item in dict:

    with open('关键词一阶段TF.txt', 'a+', encoding='utf-8') as fp:
        fp.write(item[0]+"   ")
        fp.write(str(item[1])+"   ")
        fp.write(str(item[1]/len(list)))
        fp.write("\n")