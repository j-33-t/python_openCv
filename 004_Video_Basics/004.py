#############################################
# Interactively Drawing on a Live Camera    #
#############################################


import cv2 as cv



#---------------------------------------------------------------
# LIVE DRAWING PARAMETERS
#---------------------------------------------------------------

# Callback function for rectangle
def draw_rectangle(event,x,y,flags,param):
    
    global pt1,pt2,topLeft_clicked,botRight_clicked
    
    if event == cv.EVENT_LBUTTONDOWN:
        
        # Reset Rectangle
        if topLeft_clicked == True and botRight_clicked == True:
            pt1 = (0,0)
            pt2 = (0,0)
            topLeft_clicked = False
            botRight_clicked = False
        
        if topLeft_clicked == False:
            pt1 = (x,y)
            topLeft_clicked = True
            
        elif botRight_clicked == False:
            pt2 = (x,y)
            botRight_clicked = True    

# GLOBAL VARIABLES
pt1 = (0,0)
pt2 = (0,0)
topLeft_clicked = False
botRight_clicked = False

# CONNECT to callback
WebCam = cv.VideoCapture(0)
cv.namedWindow('Test')
cv.setMouseCallback('Test', draw_rectangle)

#---------------------------------------------------------------
# DISPLAY WEBCAM VID
#---------------------------------------------------------------

while True:
    
    ret,frame = WebCam.read()
    
    # Drawing on frame based on global variables
    if topLeft_clicked == True:
        cv.circle(frame,center=pt1,radius = 2, color = (0,0,255),thickness = -1)
        
    if topLeft_clicked == True and botRight_clicked == True:
        cv.rectangle(frame, pt1,pt2,(0,0,255),2)
        
    cv.imshow('Test', frame)
    
    if cv.waitKey(1) & 0xFF == 27:
        break
    
WebCam.release()
cv.destroyAllWindows()