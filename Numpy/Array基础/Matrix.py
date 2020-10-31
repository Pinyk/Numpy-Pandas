import numpy as np
A = np.arange(2,14).reshape((3,4))
print(A)
#最小值最大值的索引
print(np.argmax(A))
print(np.argmin(A))

#平均值
print(A.mean())
print(np.average(A))
print(np.mean(A))

#逐步累加
print(np.cumsum(A))

#逐步累差
print(np.diff(A))

#找出非0的数 输出为对应的行 列索引表
print(np.nonzero(A))

#排序  对每一行进行排序
B = np.arange(14,2,-1).reshape((3,4))
print(np.sort(B))

#矩阵转置
print(np.transpose(A))
print(A.T)

#替换
#如下：使所有小于5的变为5 使所有大于9的变为9
print(np.clip(A,5,9))   #注意其余数保持不变
