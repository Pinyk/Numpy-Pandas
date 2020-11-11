import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2
plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am X')
plt.ylabel('I am Y')

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.5,-1,1.22,3],[r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])

#设置图例
#方法一    使用label设置图例
# plt.plot(x,y2,label='up')
# plt.plot(x,y1,color='red',linewidth=1,linestyle='--',label='down')
# plt.legend()

#方法二     使用plt.legend参数设置整体图例
#需要提前接受两个线条绘制后的返回值
l1, = plt.plot(x,y2)
l2, = plt.plot(x,y1,color='red',linewidth=1,linestyle='--')
plt.legend(handles=[l1,l2,],labels=['aaa','bbb'],loc='best')  #loc设置图例的位置

plt.show()