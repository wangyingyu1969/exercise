import numpy as np
import matplotlib.pyplot as plt
from skimage import data,io
import scipy.signal
import cv2 as cv

f = np.array([[1, 2, 1],
              [1, 0, 0],
              [-1, 0, 1]])
# f = np.array([[3,4,4],
# [1,0,2],
# [-1,0,3]])
img = np.array([
    [2, 3, 7, 4, 6, 2, 9],
    [6, 6, 9, 8, 7, 4, 3],
    [3, 4, 8, 3, 8, 9, 7],
    [7, 8, 3, 6, 6, 3, 4],
    [4, 2, 1, 8, 3, 4, 6],
    [3, 2, 4, 1, 9, 8, 3],
    [0, 1, 3, 9, 2, 1, 4]])


def cov2(img, f, strde):
    inw, inh = img.shape
    w, h = f.shape
    outw = (inw - w) / strde + 1
    outh = (inh - h) / strde + 1
    arr = np.zeros(shape=(outw, outh))
    for g in range(outh):
        for t in range(outw):
            s = 0
            for i in range(w):
                for j in range(h):
                    s += img[i + g * strde][j + t * strde] * f[i][j]
                    # s = img[i][j] * f[i][j]
            arr[g][t] = s
    return arr

cc=cov2(img=img,f=f,strde=1)


