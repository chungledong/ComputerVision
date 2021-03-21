import cv2
import numpy as np
import sys

img=cv2.imread('Resources/cards.jpg')
if img is None:
    sys.exit('Could not read the image')

width, height = 250, 350
top_left =[111,219]
top_right=[287,188]
bottom_left=[154,482]
bottom_right=[352,440]
pts1 = np.float32([top_left,top_right,bottom_left,bottom_right])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix.shape)
cv2.imshow('matrix',matrix)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('Image',img)
cv2.imshow('Image Output ',imgOutput)
cv2.waitKey(0)