#!/usr/bin/python

# 2.12 Lab 9
# Luke Roberto Oct 2017
# Jacob Guggenheim 2019
# Jerry Ng 2019, 2020


import numpy as np
import cv2  # OpenCV module
import time
import math
from matplotlib import pyplot as plt

def main():
    cap = cv2.VideoCapture(0)

    ret, cv_image = cap.read()    

    # otsu
    grayIm = cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)
    blurIm = cv2.GaussianBlur(grayIm,(15,5),0)
    blurThresh, otsuImage = cv2.threshold(blurIm,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # show images
    images = [blurIm, 0, otsuImage]
    plt.figure(figsize=(10, 6))
    plt.subplot(2,2,1), plt.imshow(images[0], 'gray'),
    plt.subplot(2,2,(2,4)), plt.hist(images[0].ravel(),256),  plt.axvline(x=blurThresh, color='c')
    plt.xlabel('Grayscale Pixel Intensity')
    plt.ylabel('Number of Pixels')
    plt.subplot(2,2,3), plt.imshow(images[2], 'gray')
    plt.show()
    plt.close()

if __name__=='__main__':
    main()
