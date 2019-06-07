import skimage
from skimage import io,transform
import cv2
import matplotlib.pyplot as plt
import numpy as np
img=io.imread('C:\\Users\\lenovo\\PycharmProjects\\wangyy\\roi.jpg',as_gray=True)

img_resize = cv2.resize(img,(64,64))
