import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.width',None)
data1 = pd.read_csv('D:\学习笔记\机器学习与数据挖掘\ReaderInformation.csv',encoding='gbk')
data2 = pd.read_csv('D:\学习笔记\机器学习与数据挖掘\ReaderRentRecode.csv',encoding='gbk')

res = pd.merge(data1,data2,on='num')

print(res)

res.to_csv('D:\学习笔记\机器学习与数据挖掘\merge.csv')