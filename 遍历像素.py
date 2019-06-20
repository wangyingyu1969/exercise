import cv2
import matplotlib.pyplot as plt
import numpy as np
def erzhihua(img):
    new_img = np.zeros((img.shape[0], img.shape[1]))
    rows=img.shape[0]
    cols = img.shape[1]
    for i in range(rows):
        for j in range(cols):
            new_img[i,j]=img[i,j]


    return new_img
if __name__=="__main__" :erzhihua




def access_pixels(frame):
    print(frame.shape)  # shape内包含三个元素：按顺序为高、宽、通道数
    height = frame.shape[0]
    weight = frame.shape[1]
    channels = frame.shape[2]
    print("weight : %s, height : %s, channel : %s" % (weight, height, channels))

    for row in range(height):  # 遍历高
        for col in range(weight):  # 遍历宽
            for c in range(channels):  # 便利通道
                pv = frame[row, col, c]
                frame[row, col, c] = 255 - pv  # 全部像素取反，实现一个反向效果
    return frame


img=cv2.imread('roi.jpg')
a=access_pixels(img)



plt.imshow(a)
plt.show()