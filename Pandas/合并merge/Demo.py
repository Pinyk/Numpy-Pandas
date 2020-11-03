import numpy as np
import pandas as pd

left = pd.DataFrame({
    'key':['K0','K1','K2','K3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
})

right = pd.DataFrame({
    'key':['K0','K1','K2','K4'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']
})

print(left)

#根据key列来合并  key不同的直接去除那一行
res = pd.merge(left,right,on='key')
print(res)

#考虑两个key情况
left1 = pd.DataFrame({
    'key1':['K0','K0','K1','K2'],
    'key2':['K0','K1','K0','K1'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
})

right1 = pd.DataFrame({
    'key1':['K0','K1','K1','K2'],
    'key2':['K0','K0','K0','K0'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']
})

print(left1)
print(right1)

#相当于数据库连接   inner left right outer
#indicator=True:加一列标识连接的数据在两张表的情况  也可以改默认列名 indicator=“**”
res1 = pd.merge(left1,right1,on=['key1','key2'],how='inner',indicator=True)  #内连接
print(res1)

#也可以使用行连接 index 也有四种模式inner left right outer
left2 = pd.DataFrame({
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']
},index=['a','b','c','d'])

right2 = pd.DataFrame({
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3']
},index=['a','c','d','e'])
res2 = pd.merge(left2,right2,left_index=True,right_index=True,how='outer')
print(res2)


#合并时候区分名字相同，内容不同的列
boys = pd.DataFrame({
    'k':['K0','K1','K2'],
    'age':[1,2,3]
})
girls = pd.DataFrame({
    'k':['K0','K1','K2'],
    'age':[4,5,6]
})

#自己设置列名  不设置系统会默认设置
res3 = pd.merge(boys,girls,on='k',suffixes=['_boy','_gril'],how='inner')
print(res3)