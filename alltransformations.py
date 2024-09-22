import numpy as np
import cv2 as cv

img = cv.imread('image.png')
cv.imshow('original',img)

rows, cols = img.shape[:2]

res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
cv.imshow('scaling',res)

M2 = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst2 = cv.warpAffine(img,M2,(cols,rows))
cv.imshow('rotated', dst2)

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('translate', dst)
