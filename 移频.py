# numpy.fft模块中的fftshift函数可以将FFT输出中的直流分量移动到频谱的中央。ifftshift函数则是其逆操作。
import numpy as np
import cv2
from matplotlib.pyplot import plot, show
# wave=cv2.imread('U.jpg',0)
# # x = np.linspace(0, 2 * np.pi, 30)
# # wave = np.cos(x) # 创建一个包含30个点的余弦波信号。
# transformed = np.fft.fft(wave) # 使用fft函数对余弦波信号进行傅里叶变换。
# shifted = np.fft.fftshift(transformed)  # 使用fftshift函数进行移频操作。
# # orignal=(np.all((np.fft.ifftshift(shifted) - transformed)<10**-9))
# print(np.all((np.fft.ifftshift(shifted) - transformed) < 10 ** -9)) # 用ifftshift函数进行逆操作，这将还原移频操作前的信号。
# plot(transformed, lw=2)
# # plot(shifted, lw=3)
# show()  # 使用Matplotlib分别绘制变换和移频处理后的信号。
# freqs = np.fft.fftfreq(9, d=1./9).reshape(3, 3)

freqs1=np.array([[ 0.,  1.,  2.],[ 3.,  4., -4.],[-3., -2., -1.]])
freqs2=np.array([[ 100.,  1.,  2.],[ 300.,  4., -4.],[-3., -2., -1.]])
# print=( np.fft.ifftshift(np.fft.fftshift(freqs)))

transformed1 = np.fft.fft(freqs1)
transformed2 = np.fft.fft(freqs2)
result1=np.matmul(transformed1,transformed2)
print(abs(np.fft.ifftshift(np.fft.fftshift(result1))))
print(np.matmul(freqs1,freqs2))