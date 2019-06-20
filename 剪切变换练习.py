

def tic():
    #Homemade version of matlab tic and toc functions
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print("Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds.")
    else:
        print("Toc: start time not set")

import numpy as np
from scipy import ndimage as img
import cv2
import matplotlib.pyplot as plt
import pyshearlab
import skimage

img = cv2.imread(r'C:\Users\lenovo\PycharmProjects\wangyy\barbara.jpg',0)  #加r必须否则无法读图
print(img.shape)

# 第二步：进行float32形式转换
float32_img = img

# 第三步: 使用cv2.dft进行傅里叶变化
dft_img=np.empty([512,512])
dft_img1=np.empty([512,512])
dft_img2=np.empty([512,512])
dft_img3=np.empty([512,512])

dft_img = cv2.pyrDown(float32_img,dst=dft_img)
dft_img1 = cv2.pyrDown(dft_img,dst=dft_img1)
dft_img2 = cv2.pyrDown(dft_img1,dst=dft_img2)
dft_img3 = cv2.pyrDown(dft_img2,dst=dft_img3)


plt.imshow(dft_img2)
plt.show()
# 第四步：使用np.fft.shiftfft()将变化后的图像的低频转移到中心位置
# dft_img_ce = np.fft.fftshift(dft_img)

# 第五步：使用cv2.magnitude将实部和虚部转换为实部，乘以20是为了使得结果更大
# img_dft = 20 * np.log(cv2.magnitude(dft_img_ce[:, :, 0], dft_img_ce[:, :, 1]))

# 第六步：进行画图操作
# plt.subplot(121)
# plt.imshow(img, cmap='gray')
# plt.subplot(122)
# plt.imshow(img_dft, cmap='gray')
# plt.show()
# tic()
# print("--Testing adjoint")
# print("loading image...")
#
# sigma = 30
# scales = 4
# thresholdingFactor = 3
#
# # load data
# X=img_dft
# # X = cv2.imread(r"C:\Users\lenovo\PycharmProjects\wangyy\chess.jpg")[:,:,0]
# X = X.astype(float)
# # add noise
# Xnoisy = X + sigma*np.random.randn(X.shape[0], X.shape[1])
# toc()
#
# tic()
# print("generating shearlet system...")
# ## create shearlets
# shearletSystem = pyshearlab.SLgetShearletSystem2D(0,X.shape[0], X.shape[1], scales)
#
# toc()
# tic()
# print("decomposition, thresholding and reconstruction...")
#
# # decomposition
# coeffs = pyshearlab.SLsheardec2D(Xnoisy, shearletSystem)
#
# # thresholding
# oldCoeffs = coeffs.copy()
# weights = np.ones(coeffs.shape)
#
# # reconstruction
# Xadj = pyshearlab.SLshearadjoint2D(coeffs, shearletSystem)
#
# # Validate adjoint equation
# print('<Ax, Ax> = {}, <x, AtAx> = {}, should be equal'.format(
#         np.vdot(coeffs, coeffs), np.vdot(Xnoisy, Xadj)))
# plt.imshow(Xadj)
# plt.show()