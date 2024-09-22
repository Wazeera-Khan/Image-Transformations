import numpy as np
import cv2 as cv

img = cv.imread('image.png')
cv.imshow('original',img)

rows, cols = img.shape[:2]

M2 = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst2 = cv.warpAffine(img,M2,(cols,rows))
cv.imshow('rotated', dst2)
