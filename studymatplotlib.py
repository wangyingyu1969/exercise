import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 50)  # 线性生成-1到1合计50个点
y2 = x**2
y1 = 2*x+1
plt.figure('二次函数曲线')
plt.plot(x,y1)
plt.plot(x,y2,color='red',linestyle='--',linewidth='4')
plt.xlabel('i am X')
plt.ylabel('i am Y')
# new_ticks=np.linspace(-5.5,5)
# plt.xticks(ticks=new_ticks)





plt.show()

# plt.plot(x, y1)
# new_ticks2=np.linspace(-3,3,10)
# plt.xticks(ticks=new_ticks2)
# plt.figure('一次直线方程')
# plt.plot(x, y2)
# plt.plot(x,y1,color='red',linewidth="3",linestyle='--')

# plt.xlim((-2,2))
# plt.ylim((-2,3))
# plt.xlabel('X axis')
# new_ticks=np.linspace(-2,2,10)
# plt.xticks(ticks=new_ticks)
# plt.yticks([3,1.5,1],['$really bad$','bad','good'])
# ax1= plt.gca()
# ax1.spines['right'].set_color('none')
# ax1.spines['top'].set_color('none')
# ax1.xaxis.set_ticks_position('bottom')
# ax1.yaxis.set_ticks_position('left')
# ax1.spines['bottom'].set_position(('data',-1))
# plt.show()
