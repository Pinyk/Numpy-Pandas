import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y = 2*x + 1
z = x
plt.plot(x,z)
plt.plot(x,y)
#显示在同一坐标轴上
plt.show()