# 1）程序1）删除一个图形矩阵的偶数行 偶数列
#2)程序2）放大一个图形矩阵一倍，在偶数行插入原矩阵的平均值，偶数列同样
import numpy as np
import math

# 1
def delete(array):
    array_1=np.array(array)
    list_1=[]
    for i in range(math.floor(np.shape(array_1)[1]/2)):
        list_1.append(2*i+1)
    array_1=np.delete(array_1, list_1, axis=1)
    array_1=np.delete(array_1, list_1, axis=0)
    return  array_1

#2
def insert(array):
    array_2=np.array(array)
    list_2=[]
    list_3=[]
    for i in range(1,math.floor(np.shape(array_2)[1])+1):
        list_2.append(i)
    for i in range(1,math.floor(np.shape(array_2)[0])+1):
        list_3.append(i)
    array_2=np.insert(array_2, list_2,np.mean(array_2), axis=1)
    array_2=np.insert(array_2, list_3,np.mean(array_2), axis=0)
    return  array_2

