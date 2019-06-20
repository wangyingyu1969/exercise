import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('C:\\Users\\lenovo\\PycharmProjects\\wangyy\\roi.jpg')
img=np.array(img,dtype=float)
angle=60
def rotatecordiate(angle,rect):
    angle=angle*np.pi/180
    n=img.shape[0]
    m=img.shape[1]
def onepoint(x,y):
        # X = x*math.cos(angle) - y*math.sin(angle)-0.5*n*math.cos(angle)+0.5*m*math.sin(angle)+0.5*n
        # Y = y*math.cos(angle) + x*math.sin(angle)-0.5*n*math.sin(angle)-0.5*m*math.cos(angle)+0.5*m
    X = x * np.cos(angle) - y * np.sin(angle) - 0.5 * n * np.cos(angle) + 0.5 * m * np.sin(angle) + 0.5 * n
    Y = y * np.cos(angle) + x * np.sin(angle) - 0.5 * n * np.sin(angle) - 0.5 * m * np.cos(angle) + 0.5 * m
    return [int(X),int(Y)]
newrect=[]
for i in range(4):
    point=onepoint(rect[i*2],rect[i*2+1])
    newrect.extend(point)
    newrect.extend([1])
    print(newrect)

rotatecordiate(angle=60,rect=img)
