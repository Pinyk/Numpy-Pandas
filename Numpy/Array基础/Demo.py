import numpy as np

#创建数组
a = np.array([2,1,3])
print(a)    #输出类似无逗号列表

#添加类型  int float等
b = np.array([2,1,3],dtype=np.int)
print(b.dtype)

#定义二维矩阵
array = np.array([[1,2,3],
                 [1,2,3]])
print(array)

#定义全零矩阵
arrayzeros = np.zeros((3,4),dtype=int)
# print(arrayzeros.dtype)
print(arrayzeros)

#定义全1矩阵
arrayones = np.ones((3,4),dtype=int)
print(arrayones)

#定义空矩阵（值接近为0）
arrayempty = np.empty((3,4))
print(arrayempty)

#生成有序array
##默认步长为1  左闭右开
arangedemo1 = np.arange(10,20,2)
print(arangedemo1)
##二维
arangedemo2 = np.arange(12).reshape((3,4))
print(arangedemo2)
##等差数列
arangedemo3 = np.linspace(1,10,5)
print(arangedemo3)
arangedemo3 = np.linspace(1,10,6).reshape((2,3))
print(arangedemo3)




