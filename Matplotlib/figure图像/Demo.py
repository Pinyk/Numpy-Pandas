import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2

#创建一个figure窗口
plt.figure()
plt.plot(x,y1)

#再创建一个figure窗口 独立于上一个
plt.figure(num=3,figsize=(8,5))    #num设置窗口序号 figsize设置窗口大小
plt.plot(x,y2)

#在当前窗口再加一条线
#color:颜色 linewidth:宽度 linestyle:线的风格
plt.plot(x,y1,color='red',linewidth=1,linestyle='--')
plt.show()
