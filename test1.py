import numpy as np
import cv2

img=cv2.imread('016017.png')
print(img.shape)
img=img-1
print(img)
cv2.imshow('img',img)
cv2.waitKey()