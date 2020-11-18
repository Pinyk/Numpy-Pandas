import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = 2*x + 1

plt.figure(num=1,figsize=(8,5),)
plt.plot(x,y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

#设置某一个点
x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0,y0,color='b')
#用虚线连接坐标轴
plt.plot([x0,x0],[y0,0],'k--',lw=2.5)   #lw宽度  k颜色  --：虚线


#标注
#方法一
plt.annotate(r'$2x+1=%s$'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),textcoords='offset points',
             fontsize=16,arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))

#方法二
plt.text(-3.75,3,r"$This\ is\ the\ some\ text.\ \mu\sigma_i$",fontdict={'size':16,'color':'r'})

plt.show()