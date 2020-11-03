import pandas as pd
import numpy as np

#生成从20201101开始的6个日期
dates = pd.date_range('20201101',periods=6)
print(dates)

#创建二维对象  随机生成一个6行4列的矩阵  然后为其行和列取名
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['a','b','c','d'])

df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan

print(df)

#出现null直接丢掉该行或列（axis 1：列  0：行）
print(df.dropna(axis=0,how='any'))  #how={'any','all'}  any是该行或列有一个为空就舍弃 all所有为空再舍弃

#出现null的数据位填值  填0
print(df.fillna(value=0))

#打印每一个地方是否缺失  缺失为true 不缺失false
print(df.isnull())
#如果表格过大 想要判断里面是否存在缺失值
print(np.any(df.isnull()) == True)   #说明至少有一个丢失值