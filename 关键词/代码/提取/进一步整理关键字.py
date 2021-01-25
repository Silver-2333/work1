# -*- coding:utf-8 -*-

list=open("关键词一阶段TF.txt",encoding="utf-8").read().split()
list1=[]
print(list)
for i in range(0,len(list),3):
    if len(str(list[i]))!=1 and (not str(list[i]).isdigit()):
        list1.append(list[i])
        list1.append(list[i+1])
print(list1)
num=0
for i in range(1,len(list1),2):
    num=num+(int)(list1[i])
for i in range(0,len(list1),2):
    with open('关键词一阶段TF处理.txt', 'a+', encoding='utf-8') as fp:
        fp.write(list1[i]+"   ")
        fp.write(str(list1[i+1])+"   ")
        fp.write(str((int)(list1[i+1])/num))
        fp.write("\n")