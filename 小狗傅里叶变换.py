


import numpy as np
import matplotlib.pyplot as plt
from skimage import io,color


oringnalImg=io.imread('小猫.jpg',as_gray=False)
myImg1=color.rgb2gray(oringnalImg)
# myImg=np.eye(256)
myImg=np.fft.ifftshift(myImg1)
f=np.fft.fft2(myImg)  #用FFT函数转换频域
cartesian_spectrum=20*np.log(np.abs(f))
fshift=np.fft.fftshift(f)
pseudo_spectrum=20*np.log(np.abs(fshift))


img_f = np.imag(f)
real_f=np.real(f)
img_back=np.fft.ifft2(img_f)
img_back=np.abs(img_back)
real_back=np.fft.ifft2(real_f)
real_back=np.abs(real_back)

plt.subplot(2,3,1)        #原图
plt.imshow(myImg)
plt.title('original image')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,2)          #笛卡尔坐标系图
plt.imshow(cartesian_spectrum)
plt.title('cartesion coordinate')
plt.xticks([])
plt.yticks([])

plt.subplot(2,3,3)         #伪极网格坐标系图
plt.imshow(pseudo_spectrum)
plt.title('pseudo coordinate')
plt.xticks([]),plt.yticks([])

plt.subplot(2,3,4)         #傅里叶实部图
plt.imshow(real_f)
plt.title('real_parts_spect')
plt.xticks([]),plt.yticks([])

plt.subplot(2,3,5)         #傅里叶虚部图
plt.imshow(img_f)
plt.title('imaginary parts_spect ')
plt.xticks([]),plt.yticks([])

plt.subplot(2,3,6)         #转换后回来的原图
plt.imshow(real_back)
plt.title('real_part_image')
plt.xticks([]),plt.yticks([])


plt.show()