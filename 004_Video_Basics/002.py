#########################
# Open video files      #
#########################

import cv2 as cv

import time

vid = cv.VideoCapture("../DATA/video_capture.mp4")

# Checking if file is readable

if vid.isOpened() == False:
    print("Error file not found or wrong codec")

while vid.isOpened():
    ret,frame = vid.read()
    
    
    # Display as Original
    
    if ret == True:
        
        # Showing with 30 fps , displaying with delay 1 second / Frames per second
        time.sleep(1/30)
        
        cv.imshow("frame",frame)
    
        if cv.waitKey(1) & 0xFF == 27:  #27 == esc key
            break
    
    else:
        break

vid.release()

cv.destroyAllWindows()

    