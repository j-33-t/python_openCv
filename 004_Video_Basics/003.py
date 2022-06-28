###############################
# Drawing on a Live Camera    #
###############################


import cv2 as cv

WebCam = cv.VideoCapture(0)

width , height = int(WebCam.get(cv.CAP_PROP_FRAME_WIDTH)),int(WebCam.get(cv.CAP_PROP_FRAME_HEIGHT))


### DRAWING PARAMETERS

# TOP LEFT CORNER
x = width // 2
y = height // 2

# Width and Height of Rectangle

w = width // 4
h = height // 4

# BOTTOM RIGHT CORNER [x + w, y + h]


### DISPLAY WEBCAM VID

while True:
    
    ret,frame = WebCam.read()
    
    cv.rectangle(frame,(x,y),(x + w, y + h), color=(0,0,255), thickness = 4)
    
    cv.imshow('frame', frame)
    
    if cv.waitKey(1) & 0xFF == 27:
        break
    
WebCam.release()
cv.destroyAllWindows()