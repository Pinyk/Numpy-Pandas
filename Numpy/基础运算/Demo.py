import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)

#减法 加法
c = a - b
d = a + b
print(c)
print(d)

#乘法
e = a * b
print(e)

#平法
e = a ** 2
print(e)

#三角函数 sin cos tan...
e = 10 * np.sin(a)
print(e)

#根据表达式判断数组值  成立则为true
print(b)
print(b < 3)
print(b == 3)

#矩阵乘法 （不是直接乘）
array1 = np.array([[1,1],
                  [0,1]])
array2 = np.arange(4).reshape((2,2))

print(array1)
print(array2)

array3 = array1 * array2    #对应位置值相乘
array3_dot = np.dot(array1,array2)   #矩阵乘法
#array3_dot = array1.dot(array2)  效果相同

print(array3)
print(array3_dot)

#随机生成矩阵 用函数求值
rans = np.random.random((2,4)) #随机生成范围在0到1的2行4列矩阵
print(rans)

ran = np.arange(8).reshape((2,4))
print(ran)
print(np.sum(ran)) #所有值总和
print(np.sum(ran,axis=0)) #每一列总和
print(np.sum(ran,axis=1)) #每一行总和

print(np.min(ran))
print(np.min(ran,axis=0))
print(np.min(ran,axis=1))

print(np.max(ran))
print(np.max(ran,axis=0))
print(np.max(ran,axis=1))

print(np.mean(ran))
print(np.mean(ran,axis=0))
print(np.mean(ran,axis=1))


