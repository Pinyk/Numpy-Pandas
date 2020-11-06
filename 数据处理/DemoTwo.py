import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#显示中文标签
plt.rcParams['axes.unicode_minus']=False

data = pd.read_csv('D:\学习笔记\机器学习与数据挖掘\西安北京年薪数据.csv',encoding='gbk')
data1 = data.dropna(axis=0,how='any')

print(data1.mean())     #计算北京和西安均值

print(data1.var())      #计算北京和西安方差

print(data1.std())      #计算北京和西安标准

print(data1)

print(data1.iloc[:,0])

#箱体图
fig,axes=plt.subplots(1,2,sharey=True)
sns.boxplot(x="西安",data=data1,ax=axes[0])
sns.boxplot(x="北京",data=data1,palette="Set3",ax=axes[1])
# data1.boxplot(sym='r*',vert=False,patch_artist=True,meanline=False,showmeans=True)

#小提琴图
fig,axes=plt.subplots(1,2,sharey=True)
sns.violinplot(x="西安",data=data1,ax=axes[0])
sns.violinplot(x="北京",data=data1,palette="Set3",ax=axes[1])

plt.show()
