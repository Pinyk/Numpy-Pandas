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

# 网络类型各占的比例
typeOne = data['网络类型']
arrayOne = {}
set_net = set(typeOne)
print(set_net)
for i in set_net:
    arrayOne[i] = 0
for i in typeOne:
    arrayOne[i] = arrayOne[i]+1
print(arrayOne)
labelOne = []
numberOne = []
for i in set_net:
    labelOne.append(i)
    numberOne.append(arrayOne[i])
explode = [0.1, 0.1, 0.1]
plt.pie(numberOne, labels=labelOne, explode=explode, autopct='%1.2f%%')
plt.show()



# 用户类型各占的比例
type = data['用户类型']
array = {}
set_People = set(type)
print(set_People)
for i in set_People:
    array[i] = 0
for i in type:
    array[i] = array[i]+1
print(array)
label = []
number = []
for i in set_People:
    label.append(i)
    number.append(array[i])
explode = [0.1, 0.1]
plt.pie(number, labels=label, explode=explode, autopct='%1.2f%%')
plt.show()
