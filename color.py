import cv2
import numpy as np

img = cv2.imread('4694205.jpg')

Size = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
Blur = cv2.GaussianBlur(img, (9, 9), 0)
original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to Grayscale
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

# Show the images side-by-side
cv2.imshow('Result', img)
cv2.waitKey(0)

cv2.imshow('Result', Size)
cv2.waitKey(0)

cv2.imshow('Result', Blur)
cv2.waitKey(0)

cv2.imshow('Result', original)
cv2.waitKey(0)

cv2.imshow('Result', gray)
cv2.waitKey(0)


