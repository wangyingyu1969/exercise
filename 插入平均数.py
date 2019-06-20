import numpy as np
def mean_array(image):
    mean=image.mean()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] >=mean:
                image[i][j]=mean
            else:
                pass
    return image
image=np.array([[6,2,3,8],[4,5,6,0],[7,8,9,9]])
print(mean_array(image))
