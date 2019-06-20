import numpy as np


def Cov(img,f,stride):
    w,h=f.shape
    imw,imh=img.shape
    outh=(imh-h)/stride+1
    outw=(imw-w)/stride+1
    new_arr=np.zeros([5,5])
    for g in range(outh):
        for k in range(outw):
            s=0
            for j in range(w):
                for i in range(h):
                    s +=img[i+g*stride][j+k*stride]*f[i][j]
            new_arr[g][k]=s
    return new_arr
f1 = np.array([[1, 2, 1],
              [1, 0, 0],
              [-1, 0, 1]])
f2=np.array([[1,2,3],[4,6,2],[4,5,6]])
myimg = np.array([
    [2, 3, 7, 4, 6, 2, 9],
    [6, 6, 9, 8, 7, 4, 3],
    [3, 2, 4, 1, 9, 8, 3],
    [0, 1, 3, 9, 2, 1, 4]])
mul= np.dot(f1[1],f2[1])
print(mul)

