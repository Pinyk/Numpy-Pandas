import pandas as pd
import numpy as np

#生成从20201101开始的6个日期
dates = pd.date_range('20201101',periods=6)
print(dates)

#创建二维对象  随机生成一个6行4列的矩阵  然后为其行和列取名
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['a','b','c','d'])
print(df)

#根据位置设置值
df.iloc[2,2] = 111
print(df)

#根据标签设置值
df.loc['20201101','b'] = 222
print(df)

#选择范围更改
# df[df.a > 4] = 0    #会改变a列大于4的所有行的值
df.a[df.a > 4] = 0    #会改变a列大于4 这一列的值  也可以前面设置df.b 通过a列的条件修改b列
print(df)

#增加一列
df['f'] = np.nan
#对应列赋值
df['e'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20201101',periods=6))
df['g'] = np.arange(6)
print(df)