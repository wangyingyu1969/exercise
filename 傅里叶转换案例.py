import cv2
import numpy as np
import matplotlib.pyplot as plt
import mkl_




# 第一步读取图

# img=np.ones([256,256],dtype=int)
img = cv2.imread('barbara.jpg',0)  #加r必须否则无法读图
# print(img.shape)

# 第二步：进行float32形式转换
float32_img = np.float32(img)

# 第三步: 使用cv2.dft进行傅里叶变化
dft_img =np.fft.fft2(float32_img)

# 第四步：使用np.fft.shiftfft()将变化后的图像的低频转移到中心位置
dft_img_ce = np.fft.fftshift(dft_img)

# 第五步：使用cv2.magnitude将实部和虚部转换为实部，乘以20是为了使得结果更大
# img_dft = 20 * np.log(cv2.magnitude(dft_img_ce[:, :, 0], dft_img_ce[:, :, 1]))

# 第六步：进行画图操作
plt.show()

