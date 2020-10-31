import numpy as np

#单行索引
A = np.arange(3,15)
print(A)
print(A[3])

#矩阵索引
B = np.arange(3,15).reshape((3,4))
print(B)
print(B[1][1])
print(B[1,1])   #同上

#冒号可以代替范围
print(B[1,:])
print(B[:,0])
print(B[1,1:3])

#for循环迭代每一行 和 每一列
for row in B:
    print(row)

for column in B.T:
    print(column)

#迭代每一个内容
print(B.flatten())   #将矩阵得到一个展开的数组

for item in A.flat:
    print(item)