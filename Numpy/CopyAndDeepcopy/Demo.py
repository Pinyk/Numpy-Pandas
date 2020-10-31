import numpy as np

a = np.array([1,2,3,4])
#简单赋值
b = a

#a发生改变时候，b也发生改变  同样 改变b a也变（浅copy）
a[0] = 0
print(a)
print(b)
print(b is a)   #如果是true说明指向相同


#要使赋值不关联之前变量  需要使用深copy方法
c = a.copy()
print(c)
c[0] = 1
print(c is a)
print(c)

