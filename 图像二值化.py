from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def erzhihua(img):
    rows, cols = img.shape
    for i in range(rows):
        for j in range(cols):
            if (img[i, j] <= 128):
                img[i, j] = 0
            else:
                img[i, j] = 1
    return img
if __name__=="__main__" :erzhihua

