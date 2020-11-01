import pandas as pd
import numpy as np

#创建一维列表
s = pd.Series([1,3,6,np.nan,44,1])    #默认是float类型
#会给每一个元素添加一个索引
print(s)

#生成从20201101开始的6个日期
dates = pd.date_range('20201101',periods=6)
print(dates)

#创建二维对象  随机生成一个6行4列的矩阵  然后为其行和列取名
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)

#默认行名和列名是0开头递增数列
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)

#字典形式创建DF
df2 = pd.DataFrame({
    'A':1.,
    'B':np.array([1,2,3]),
    'C':pd.Categorical(["test","train","test"])
})
print(df2)

#输出df每一列类型
print(df2.dtypes)

#输出行索引和列索引
print(df2.index)
print(df2.columns)

#打印df中的值
print(df2.values)

#打印df转置的值
print(df2.T)

#对行列索引进行排序
print(df2.sort_index(axis=1,ascending=False))  #对列索引倒序
print(df2.sort_index(axis=0,ascending=False))  #对行索引倒序

#对值进行排序
print(df2.sort_values(by='C'))   #对c列的值进行排序



