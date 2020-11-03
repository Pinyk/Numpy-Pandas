import numpy as np
import pandas as pd

#读取csv文件
data = pd.read_csv('D:\学习笔记\机器学习与数据挖掘\ReaderRentRecode.csv')

#直接打印  pandas自动加行索引
print(data)

data['新增属性'] = np.nan
data.iloc[0,4] = 1


print(data)
#导出csv文件
data.to_csv('D:\学习笔记\机器学习与数据挖掘\测试.csv')
