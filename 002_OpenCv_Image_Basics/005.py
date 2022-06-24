#####################################
##       MOUSE MOVEMENT          ####
#####################################

import cv2 as cv
import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#       VARIABLES
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Create a function based on a CV Event (Left button click)
drawing = False # True if mouse is pressed
ix,iy = -1,-1


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#        FUNCTION
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# mouse callback function
def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv.EVENT_LBUTTONDOWN:
        # When you click DOWN with left mouse button drawing is set to True
        drawing = True
        # Then we take note of where that mouse was located
        ix,iy = x,y

    elif event == cv.EVENT_MOUSEMOVE:
        # Now the mouse is moving
        if drawing == True:
            # If drawing is True, it means you've already clicked on the left mouse button
            # We draw a rectangle from the previous position to the x,y where the mouse is
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
           

    elif event == cv.EVENT_LBUTTONUP:
        # Once you lift the mouse button, drawing is False
        drawing = False
        # we complete the rectangle.
        cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -         
#        CREATING CANVAS FOR DRAWING        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# This names the window so we can reference it 
cv.namedWindow(winname='my_drawing')

# Connects the mouse button to our callback function
cv.setMouseCallback('my_drawing',draw_rectangle)

while True: #Runs forever until we break with Esc key on keyboard
    # Shows the image window
    cv.imshow('my_drawing',img)
    # EXPLANATION FOR THIS LINE OF CODE:
    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv-waitkey1/39201163
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
    
# Once script is done, its usually good practice to call this line
# It closes all windows (just in case you have multiple windows called)
cv.destroyAllWindows()
