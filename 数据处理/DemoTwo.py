import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#显示中文标签
plt.rcParams['axes.unicode_minus']=False

data = pd.read_csv('D:\学习笔记\机器学习与数据挖掘\西安北京年薪数据.csv',encoding='gbk')
data1 = data.dropna(axis=0,how='any')

print(data1.mean())     #计算北京和西安均值

print(data1.var())      #计算北京和西安方差

print(data1.std())      #计算北京和西安标准

data1.boxplot(sym='r*',vert=False,patch_artist=True,meanline=False,showmeans=True)

#
# plt.violinplot(data1,showmeans=True, showextrema=True, showmedians=True)

plt.show()
