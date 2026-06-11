import cv2 as cv
import sys

img = cv.imread('Ch.01/soccer.jpg')

if img is None:
    sys.exit('File Not Found')

cv.imshow('Image Display', img)

cv.waitKey()
cv.destroyWindow()