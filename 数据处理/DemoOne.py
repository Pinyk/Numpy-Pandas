import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']#显示中文标签
plt.rcParams['axes.unicode_minus']=False


data = pd.read_csv('D:\学习笔记\机器学习与数据挖掘\某县广电宽度数据.csv',encoding='gbk')
pd.set_option('display.width',None)

print(data.head())

print(np.any(data.isnull()) == True)   #数据中没有缺失值

print(data.iloc[2,0])

# print(type(data.iloc[2,12]))


# print(data[data[u'产品名称'] == '宽带10M产品'])
# print(data.head())

# grouped = data["收费类型"].groupby(by=data["客户等级"]).mean()

# print(grouped.head())

#客户等级类型数量图
df = data["客户等级"].value_counts()
print(df)
print(df.index)
plt.plot(df)
plt.show()

#产品名称类型数量图
df1 = data["产品名称"].value_counts()
print(df1)
print(df1.index)
plt.plot(df1,'ro')
plt.show()

# y = pd.Series([0,2000,4000,6000,8000,10000])
# print(y)
# ax = df1.plot.scatter(x='产品名称',y=y,color='DarkBlue',label='Class 1')
# df.plot.scatter(x='客户等级',y=y,color='DarkGreen',label='Class 2',ax=ax)
# plt.show()
