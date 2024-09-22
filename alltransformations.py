import numpy as np
import cv2 as cv

img = cv.imread('image.png')
cv.imshow('original',img)

rows, cols = img.shape[:2]

res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
cv.imshow('scaling',res)
