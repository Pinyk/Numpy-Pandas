import numpy as np

A = np.arange(12).reshape((3,4))
print(A)

#平分成2块 按列
print(np.split(A,2,axis=1))

#分成3块 按行
print(np.split(A,3,axis=0))

#不等分割
print(np.array_split(A,3,axis=1))

#另一种方法
print(np.vsplit(A,3))   #按行
print(np.hsplit(A,2))    #按列


