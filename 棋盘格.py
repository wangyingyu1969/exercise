


import numpy as np
import matplotlib.pyplot as plt
from skimage import io
image=io.imread('barbara.jpg')
print(np.mean(image))

width=512
height=512
length=40
# image = np.zeros((width,height),dtype = np.uint8)
print(image.shape[0],image.shape[1])

for j in range(50,height-50):
     for i in range(50,width-50):
         if((int)((i)/length) + (int)((j)/length))%2:
              image[i,j] = 255



plt.imsave("pulted_barbara.png",image)
print(np.mean(image))
plt.imshow(image)
plt.show()

import cv2
import random

# 读取图片
# img = cv2.imread(r'C:\Users\lenovo\PycharmProjects\wangyy\barbara.jpg')
#
# # h、w为想要截取的图片大小
# h = 80
# w = 80
#
# count = 1
# while 1:
#     # 随机产生x,y  此为像素内范围产生
#     y = random.randint(1, 512)
#     x = random.randint(1, 512)
# # 随机截图
#     cropImg = img[(y):(y + h), (x):(x + w)]
#     cv2.imwrite('mypic/' + str(count) + '.png', cropImg)
#     count += 1
#
#     if count == 2500:
#         break

