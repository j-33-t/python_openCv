from ast import While
import numpy as np
import cv2 as cv

img = cv.imread("../DATA/00-puppy.jpg")

while True:
    cv.imshow("Puppy",img)
    
    # If we waitied 1 ms AND we pressed esc key
    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()