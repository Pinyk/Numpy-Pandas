import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('D:\学习笔记\机器学习与数据挖掘\movie_metadata.csv',encoding='gbk')

print(np.any(data.isnull()) == True)  #含有缺失值

data1 = data.dropna(axis=0,how='all')  #将全为null的行剔除

data2 = data1.fillna(value=0)    #将含有null的值替换为0

print(np.any(data2.duplicated()) == True)    #含有重复行

data3 = data2.drop_duplicates()    #去重

print(np.any(data3.duplicated()) == True)   #验证去重情况

print(np.any(data3.isnull()) == True)  #验证缺失值情况

data3.to_csv('D:\学习笔记\机器学习与数据挖掘\movie_metadata1.csv')