import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

plt.rcParams['font.sans-serif']=['SimHei']#显示中文标签
plt.rcParams['axes.unicode_minus']=False

data = pd.read_csv('D:\学习笔记\机器学习与数据挖掘\iris.csv',encoding='gbk',header=None,
                   names=['a','b','c','d','type'])
pd.set_option('display.width',None)

sns.boxplot(x='type', y='a', data=data)
plt.show()

data['type'].loc[data['type'] == 'Iris-setosa'] = 0
data['type'].loc[data['type'] == 'Iris-versicolor'] = 1
data['type'].loc[data['type'] == 'Iris-virginica'] = 2

print(data)

data1 = data.iloc[:,0:4]
data2 = data.iloc[:,4]

data_1 = data1.values.tolist()
data_2 = data2.values.tolist()

print(data_1)
print(data_2)

pca = PCA(n_components=2)

res = pca.fit_transform(data_1)

print(res)

red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []

for i in range(len(res)):
    if data_2[i] == 0:
        red_x.append(res[i][0])
        red_y.append(res[i][1])

    elif data_2[i] == 1:
        blue_x.append(res[i][0])
        blue_y.append(res[i][1])

    else:
        green_x.append(res[i][0])
        green_y.append(res[i][1])

plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')

plt.show()