import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])

#上下合并
print(np.vstack((A,B)))

#左右合并
print(np.hstack((A,B)))

#将A转置  （这里注意不能用矩阵的T方法转置一维Array）
print(A[:,np.newaxis])
print(np.hstack((A[:,np.newaxis],B[:,np.newaxis])))

#后面参数为0可以左右合并  参数1可以纵向合并
C =  np.concatenate((A,B,B,A),axis=0)
print(C)


