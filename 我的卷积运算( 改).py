import  numpy as np

from scipy import signal
from skimage import  io
import matplotlib.pyplot as plt
from convkeneral import Func
img=io.imread('kewen.jpeg',as_gray=True) #创建一个灰度图像
class MyConvolutional():
    def __init__(self,a1,a2):
        self.a1=a1
        self.a2=a2
    def Convolutional_array(self):
        #外围添加一圈0
        a=np.zeros([a1.shape[0]+2, a1.shape[1]+2])
        c=[]
        d=[]
        for i in range(1,a1.shape[0]+1):
            c.append(i)
        for j in range(1,a1.shape[1]+1):
            d.append(j)
        a[np.ix_(c,d)]=a1
        # print(a)
        #遍历获取矩阵
        n_1=a2.shape[0]
        n_2=a2.shape[1]
        d_shape=a.shape[0]
        d_shape_1=a.shape[1]
        all_array=[]
        for m in range(0,d_shape-2):
            for j in range(0,d_shape_1-2):
                list_hang = []
                list_lie=[]
                for l in range(m,n_1+m):
                    list_hang.append(l)
                for k in range(j,n_2+j):
                    list_lie.append(k)
                one_array=a[np.ix_(list_hang, list_lie)]
                all_array.append(one_array)
        array_list = []
        # print(all_array)
        #计算矩阵的数值
        for one in range(0,len(all_array)):
            each_array=np.array(all_array[one])
            len_array=len(each_array)-len(a2)+1
            for i in range(len_array):
                b=np.sum(each_array[i:i+len(a2-1)]*a2)
                array_list.append(b)
        #还原卷积后的矩阵
        one_line_array =np.array(array_list)
        all_array=one_line_array.reshape([a1.shape[0],a1.shape[1]])
        return all_array

#a1是被卷积的矩阵
if __name__=="__main__" :MyConvolutional
    #a1是被卷积的矩阵
    #a2是用来卷积的矩阵

img=io.imread('kewen.jpeg',as_gray=True) #创建一个灰度图像
img=img.astype(float)
# kenerl = np.array([[-3 - 3j, 0 - 10j, +3 - 3j], [-10 + 0j, 0 + 0j, +10 + 0j], [-3 + 3j, 0 + 10j, +3 + 3j]])  # 设置一个特殊的卷积和
kenerl = Func.db3(1)


# a=MyConvolutional(img,kenerl)
# # a=np.floor(a)
#  plt.imshow(a)
#  plt.show()
# print(a)
# print(img.ndim)
# kenerl=np.array([[-3-3j,0-10j,+3-3j],[-10+0j,0+0j,+10+0j],[-3+3j,0+10j,+3+3j]]) #设置一个特殊的卷积和
# kenerl=Func.gauss4(1)
#
grad=signal.convolve2d(img,kenerl,boundary='symm',mode='same') #把图像的face数组和设计好的卷积和作二维卷积运算,设计边界处理方式为symm
print(grad.shape)
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,6)) #建立1行2列的图fig
ax1.imshow(img,cmap='gray') #显示原始的图
ax1.set_axis_off()                    #不显示坐标轴
ax2.imshow(np.absolute(grad),cmap='gray') #显示卷积后的图
ax2.set_axis_off() #不显示坐标轴

plt.show() #显示绘制好的画布

