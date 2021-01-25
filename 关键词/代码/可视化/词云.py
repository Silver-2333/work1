# -*- coding:utf-8 -*-
import wordcloud
from matplotlib.mathtext import Fonts

list=open("可视化四阶段.txt",encoding="utf-8").read().split()
list1=[]
for i in range(0,200,2):
    list1.append(list[i])
d=' '.join(list1)

c = wordcloud.WordCloud()
c.background_color="white"
c.height=2000
c.width=2000
c.colormap=None
c.font_path="C:/Windows/Fonts/STKAITI.TTF"
     #1.配置对象参数
c.generate(d)  #2.加载词云文本
c.to_file("四阶段.png")