import cv2
import numpy as np
from scipy import fft,ifft
import matplotlib.pyplot as plt
img1=plt.imread(r'C:\Users\lenovo\PycharmProjects\new\barbara.jpg')

f=np.fft.fft2(img1)  #傅里叶正转换
#要进行对数转换是因为傅里叶变换后的结果对于在显示器显示来讲范围比较大，
# 这样的话对于一些小的变化或者是高的，这时坐标中心在左上角，图上可以看见能量集中在四个角上
# magnitude_spectrum1=20*np.log(np.abs(f))
# plt.imsave("f.jpg",magnitude_spectrum1)
# fshift=np.fft.fftshift(f)  #坐标归位到中心，可以从图上看见坐标中心回到笛卡尔坐标系

#之所以要进行对数转换是因为傅里叶变换后的结果对于在显示器显示来讲范围比较大，这样的话对于一些小的变化或者是高的变换值不能进行观察
# magnitude_spectrum2=20*np.log(np.abs(fshift))
# plt.imsave('magntiude.jpg',magnitude_spectrum2)
# plt.figure(num='Tommy Experiment for Fourier Transform')
# plt.subplot(1,3,1),plt.imshow(img1)
# plt.title('original date '),plt.xticks([]),plt.yticks([])
# plt.subplot(1,3,2),plt.imshow(magnitude_spectrum1)
# plt.title('Fourier spectrum '),plt.xticks([]),plt.yticks([]),
# plt.subplot(1,3,3),plt.imshow(magnitude_spectrum2)
# plt.title('pseudo coordinate '),plt.xticks([]),plt.yticks([]),plt.yticks([])
# plt.show()

img_real=np.imag(f)
img_angle=np.angle(img_real)
plt.imshow(img_real)
plt.show()

