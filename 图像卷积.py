

import numpy as np
import matplotlib.pyplot as plt
import string
from skimage import data

srcImg = data.astronaut()

print(srcImg.shape)

test_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

fudiao_kernel = np.array([[-1, -1, 0],
                          [-1, 0, 1],
                          [0, 1, 1]])
sharp_kernel = np.array([[1, 1, 1],[1, -7, 1],[1, 1, 1]])


def generate_dst(srcImg):
    m = srcImg.shape[0]
    n = srcImg.shape[1]
    n_channel = srcImg.shape[2]

    dstImg = np.zeros((m - test_kernel.shape[0] + 1, n - test_kernel.shape[0] + 1, n_channel))
    return dstImg


def conv_2d(src, kernel, k_size):
    dst = generate_dst(src)
    print(dst.shape)
    conv(src, dst, kernel, k_size)
    return dst


def conv(src, dst, kernel, k_size):
    for i in range(dst.shape[0]):
        for j in range(dst.shape[1]):
            for k in range(dst.shape[2]):
                value = _con_each(src[i:i + k_size, j:j + k_size, k], kernel)

                dst[i, j, k] = value


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# kernel一次扫描获得的原图像VALUE
def _con_each(src, kernel):
    pixel_count = kernel.size
    pixel_sum = 0
    _src = src.flatten()
    _kernel = kernel.flatten()

    for i in range(pixel_count):
        pixel_sum += _src[i] * _kernel[i]

    value = pixel_sum / pixel_count

    value = value if value > 0 else 0

    value = value if value < 255 else 255

    # value = sigmoid(pixel_sum)

    return value


# def test_conv(src, kernel, k_size):
#     plt.figure()
#     plt.subplot(121)
#     plt.imshow(src)
#
#     dst = conv_2d(src, kernel, k_size)
#
#     plt.subplot(122)
#     plt.imshow(dst)
#
#     plt.show()
#
# test_conv()
# #def test_deep_conv(level):
#     src = srcImg
#     plt.figure()
#     plt.subplot(100 + level * 10 + 1)
#     plt.imshow(src)
#     for i in range(level - 1):
#         dst = conv_2d(src, test_kernel, 3)
#         plt.subplot(100 + level * 10 + i + 2)
#         plt.imshow(dst)
#         src = dst
#     plt.show()
#
#
# def rgb2gray(RGB):
#     return np.dot(RGB[..., :3], [0.299, 0.587, 0.144])
#
#
# #def test_more_kernel(src):
#     plt.figure()
#     plt.subplot(141)
#     plt.axis('off')
#     plt.imshow(src)
#
#     dst1 = conv_2d(src, fudiao_kernel, 3)
#
#     plt.subplot(142)
#     plt.axis('off')
#     plt.imshow(rgb2gray(dst1))
#
#     dst2 = conv_2d(src, sharp_kernel, 3)
#
#     plt.subplot(143)
#     plt.axis('off')
#     plt.imshow(rgb2gray(dst2))
#
#     dst3 = conv_2d(src, sharp_kernel, 3)
#
#     plt.subplot(144)
#     plt.axis('off')
#     plt.imshow(rgb2gray(dst3))
#
#     plt.show()
#
#
# #test_more_kernel(srcImg)
# # test_conv(srcImg,test_kerne1,3)
