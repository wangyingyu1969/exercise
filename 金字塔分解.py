import numpy as np
import tensorflow as tf
import cv2
#高斯卷积核
k = np.float32([1, 4, 6, 4, 1])
k = np.outer(k, k)
k5x5 = k[:, :, None, None] / k.sum() * np.eye(3, dtype=np.float32)
img = cv2.imread(r'C:\Users\lenovo\PycharmProjects\wangyy\roi.jpg')
img = np.float32(img)
print(k5x5)


# 这个函数将图像分为低频和高频成分
def lap_split(img):
    with tf.name_scope('split'):
        #         # 做过一次卷积相当于一次“平滑”，因此lo为低频成分，下采样
        lo = tf.nn.conv2d(img, k5x5, [1, 2, 2, 1], 'SAME')
        #         # 低频成分放缩到原始图像一样大小得到lo2，再用原始图像img减去lo2，就得到高频成分hi，上采样
        lo2 = tf.nn.conv2d_transpose(lo, k5x5 * 4, tf.shape(img), [1, 2, 2, 1])
        hi = img - lo2
        return lo, hi

#
# # lap_split(img)
# # # 这个函数将图像img分成n层拉普拉斯金字塔
# # def lap_split_n(img, n):
#     levels = []
#     for i in range(n):
#         #         # 调用lap_split将图像分为低频和高频部分
#         #         # 高频部分保存到levels中
#         #         # 低频部分再继续分解
#         img, hi = lap_split(img)
#         levels.append(hi)
#         #     # 添加低频部分
#         levels.append(img)
#         #     # 倒叙列表
#         return levels[::-1]
#
#
# # 将拉普拉斯金字塔还原到原始图像
# # def lap_merge(levels):
#     img = levels[0]
#     for hi in levels[1:]:
#         with tf.name_scope('merge'):
#             img = tf.nn.conv2d_transpose(img, k5x5 * 4, tf.shape(hi), [1, 2, 2, 1]) + hi
#     return img
#



