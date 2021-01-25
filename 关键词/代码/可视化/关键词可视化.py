# -*- coding:utf-8 -*-

list=open("最终关键字/关键词三阶段TF处理.txt",encoding="utf-8").read().split()
list1=open("IDF/三阶段IDF2.txt",encoding="utf-8").read().split()
keyword_list=[]
idf_list=[]
for i in range(0,300,3):
    keyword_list.append(str(list[i]))
    idf_list.append((str(list1[i+1])))
dict = {};
for item in keyword_list:
    a=keyword_list.index(item)
    b=idf_list.index(item)
    dict[item]=a*0.6+b*0.4

dict=sorted(dict.items(), key = lambda kv:(kv[1], kv[0]))

for item in dict:

    with open('可视三阶段.txt', 'a+', encoding='utf-8') as fp:
        fp.write(item[0]+"   ")
        fp.write(str(item[1]))
        fp.write("\n")