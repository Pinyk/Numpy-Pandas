import pandas as pd
import numpy as np

#生成从20201101开始的6个日期
dates = pd.date_range('20201101',periods=6)
print(dates)

#创建二维对象  随机生成一个6行4列的矩阵  然后为其行和列取名
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['a','b','c','d'])
print(df)

#输出a索引的列  两种方法
print(df.a)
print(df['a'])

#输出行  切片
print(df[0:1])
print(df[0:3])
# print(df['20201101','20201103'])   报错

#根据标签选择
#输出20201101这一行
print(df.loc['20201101'])

#输出所有行  对应的ab列
print(df.loc[:,['a','b']])

#输出某一行  对应的ab列
print(df.loc['20201101',['a','b']])

#使用位置信息来选择  类似numpy
print(df.iloc[3])  #打印第三行数据
print(df.iloc[3,1])  #第3行第1列
print(df.iloc[3:5,1:3])  #切片
print(df.iloc[[1,3,5],1:3])  #间隔筛选

#标签和位置结合使用  弃用
# print(df.ix[:3,['a','c']])

#真值筛选
print(df)
print(df[df.a > 8])        #只对比a然后输出符合a条件的所有数据



