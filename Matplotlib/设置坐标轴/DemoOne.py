import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2

plt.figure(num=3,figsize=(8,5))
plt.plot(x,y2)

plt.plot(x,y1,color='red',linewidth=1,linestyle='--')

#设置x y轴的范围
plt.xlim((-1,2))
plt.xlim((-2,3))

#设置坐标名字
plt.xlabel('I am X')
plt.ylabel('I am Y')

#替换坐标轴坐标
new_ticks = np.linspace(-1,2,5)
print(new_ticks)

plt.xticks(new_ticks)
# plt.yticks([-2,-1.5,-1,1.22,3],['really bad','bad','normal','good','really good'])
#换字体
plt.yticks([-2,-1.5,-1,1.22,3],[r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])

#设置坐标轴位置
ax = plt.gca()   #获取整个坐标轴
#ax.spines  获取4条边框
ax.spines['right'].set_color('none')   #去除上右边框
ax.spines['top'].set_color('none')

#设置默认的x y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#移动x y轴位置
ax.spines['bottom'].set_position(('data',0))  #将x轴绑定在y=0位置
ax.spines['left'].set_position(('data',0))  #将y轴绑定在x=0位置

plt.show()
