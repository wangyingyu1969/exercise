import cv2
image=cv2.imread(r'C:\Users\lenovo\PycharmProjects\wangyy\roi.jpg')

def slice_image(image, stride, image_size):
    # 切分一行图片,长条图片
    def slice_image_y(image, stride, image_size):
        h, _, _ = image.shape
        image_list = []
        for i in range(0, h, stride):
            if i + image_size > h:
                im = image[-image_size:, :, :]
            else:
                im = image[i:i + image_size, :, :]
            image_list.append(im)
        return image_list

slice_image(image,stride='20',image_size=512*512)

# 作者：onexming
# 来源：CSDN
# 原文：https://blog.csdn.net/qq_39124762/article/details/84346887
# 版权声明：本文为博主原创文章，转载请附上博文链接！