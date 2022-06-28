import cv2 as cv
# Create a function based on a CV2 Event (Left button click)

# mouse callback function
def draw_circle(event,x,y,flags,param):

    global center,clicked

    # get mouse click on down and track center
    if event == cv.EVENT_LBUTTONDOWN:
        center = (x, y)
        clicked = False
    
    # Use boolean variable to track if the mouse has been released
    if event == cv.EVENT_LBUTTONUP:
        clicked = True

        
# Haven't drawn anything yet!
center = (0,0)
clicked = False


# Capture Video
WebCam = cv.VideoCapture(0) 

# Create a named window for connections
cv.namedWindow('Test')

# Bind draw_rectangle function to mouse cliks
cv.setMouseCallback('Test', draw_circle) 


while True:
    # Capture frame-by-frame
    ret, frame = WebCam.read()

    # Use if statement to see if clicked is true
    if clicked==True:
        # Draw circle on frame
        cv.circle(frame, center=center, radius=175, color=(255,0,0), thickness=5)
        
    # Display the resulting frame
    cv.imshow('Test', frame)

    # This command let's us quit with the "esc" button on a keyboard.
    if cv.waitKey(1) & 0xFF == 27:
        break

# When everything is done, release the capture
WebCam.release()
cv.destroyAllWindows()