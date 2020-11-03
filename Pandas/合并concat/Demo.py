import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])

# print(df1)
# print(df2)
# print(df3)

#上下合并 ignore_index=True:行索引重新排序
res = pd.concat([df1,df2,df3], axis=0,ignore_index=True)  #竖向合并
print(res)

#join ['inner','outer']
df4 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df5 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
print(df4)
print(df5)

#默认使用outer的模式连接
res1 = pd.concat([df4,df5],axis=0)  #由于索引不同  直接合并会导致增加列  无值的列用nan来填充
print(res1)

#使用inner模式连接    类似于数据库表连接  丢掉不相干的值
res2 = pd.concat([df4,df5],axis=0,join='inner',ignore_index=True)
print(res2)

#左右合并 join_axes
# res3 = pd.concat([df4,df5],axis=1,join_axes=[df4.index])
# print(res3)   弃用

#append 上下合并
res3 = df1.append(df2,ignore_index=True)
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res4 = res3.append(s1,ignore_index=True)   #增加单行数据
print(res4)







