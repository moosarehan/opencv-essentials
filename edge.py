import cv2
import numpy as np
img = cv2.imread('images/istockphoto-627966690-612x612.jpg')

edge=cv2.Canny(img,100,200)
kernel = np.ones((3, 3), dtype=np.uint8)
edge_d=cv2.dilate(edge,kernel)
edge_e=cv2.erode(edge_d,kernel)
cv2.imshow('edge',edge)
cv2.imshow('dilate',edge_d)
cv2.imshow('erode',edge_e)
cv2.waitKey(0)


