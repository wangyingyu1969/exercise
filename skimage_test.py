from skimage import io,transform,data

import numpy as np
import matplotlib.pyplot as plt
im= data.astronaut()
# im1=transform.resize(im,(250,250))
srcImg=io.imread('C:\\Users\\lenovo\\PycharmProjects\\wangyy\\roi.jpg',as_gray=False)

print(srcImg)

# m = srcImg.shape[0]
# n = srcImg.shape[1]
# n_channel = srcImg.shape[2]
# test_kernel = np.array([[-1, -1, -1],
#                         [-1, 9, -1],
#                         [-1, -1, -1]])
#
# dstImg = np.zeros((m - test_kernel.shape[0] + 1, n - test_kernel.shape[0] + 1, n_channel))
# print (dstImg.shape[0])
# print ('the o shape is %d'%m)