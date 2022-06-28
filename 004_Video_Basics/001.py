
#########################
# Connecting to camera  #
#########################

import cv2 as cv

Webcam = cv.VideoCapture(0)

width, height = int(Webcam.get(cv.CAP_PROP_FRAME_WIDTH)) , int(Webcam.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = 24
# Saving Video
# --- XVID for mac/ubuntu 
# --- DIVX for Windows
writer = cv.VideoWriter('video_basics.mp4', cv.VideoWriter_fourcc(*'XVID'),fps,(width,height)) 

# Display Video

while True:
    ret,frame = Webcam.read()
    
    # Reading as GrayScale
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Operations [adding frames to the mp4 file]
    writer.write(frame)
    
    # Display as Original
    cv.imshow("frame",frame)
    
    # Display as Grayscale
    # cv.imshow("frame",gray)
    
    
    
    if cv.waitKey(1) & 0xFF == 27:  #27 == esc key
        break
    

Webcam.release()
writer.release()
cv.destroyAllWindows()

    