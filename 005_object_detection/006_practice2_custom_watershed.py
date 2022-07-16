import cv2
import numpy as np
import matplotlib.pyplot as plt
messi_ronaldo = cv2.imread('../DATA/messi-ronaldo.jpeg')
messi_ronaldo_copy = np.copy(messi_ronaldo)
plt.imshow(messi_ronaldo);
messi_ronaldo.shape
messi_ronaldo.shape[:2]
marker_image = np.zeros(messi_ronaldo.shape[:2],dtype=np.int32)
segments = np.zeros(messi_ronaldo.shape,dtype=np.uint8)
segments.shape


### Create colors for Markers


from matplotlib import cm

cm.tab10(0)
cm.tab10(1)
np.array(cm.tab10(0))
np.array(cm.tab10(0))[:3]
np.array(cm.tab10(0))[:3]*255
x = np.array(cm.tab10(0))[:3]*255
x.astype(int)
tuple(x.astype(int))

# Let's make a function for all those steps
def create_rgb(i):
    x = np.array(cm.tab10(i))[:3]*255
    return tuple(x)
colors = []
# One color for each single digit
for i in range(10):
    colors.append(create_rgb(i))
colors
### Setting Up Callback Function
# Numbers 0-9
n_markers = 10
# Default settings
current_marker = 1
marks_updated = False
def mouse_callback(event, x, y, flags, param):
    global marks_updated 

    if event == cv2.EVENT_LBUTTONDOWN:
        
        # TRACKING FOR MARKERS
        cv2.circle(marker_image, (x, y), 10, (current_marker), -1)
        
        # DISPLAY ON USER IMAGE
        cv2.circle(messi_ronaldo_copy, (x, y), 10, colors[current_marker], -1)
        marks_updated = True

cv2.namedWindow('messi_ronaldo Image')
cv2.setMouseCallback('messi_ronaldo Image', mouse_callback)

while True:
    
    # SHow the 2 windows
    cv2.imshow('WaterShed Segments', segments)
    cv2.imshow('messi_ronaldo Image', messi_ronaldo_copy)
        
        
    # Close everything if Esc is pressed
    k = cv2.waitKey(1)

    if k == 27:
        break
        
    # Clear all colors and start over if 'c' is pressed
    elif k == ord('c'):
        messi_ronaldo_copy = messi_ronaldo.copy()
        marker_image = np.zeros(messi_ronaldo.shape[0:2], dtype=np.int32)
        segments = np.zeros(messi_ronaldo.shape,dtype=np.uint8)
        
    # If a number 0-9 is chosen index the color
    elif k > 0 and chr(k).isdigit():
        # chr converts to printable digit
        
        current_marker  = int(chr(k))
        
        # CODE TO CHECK INCASE USER IS CARELESS
#         n = int(chr(k))
#         if 1 <= n <= n_markers:
#             current_marker = n
    
    # If we clicked somewhere, call the watershed algorithm on our chosen markers
    if marks_updated:
        
        marker_image_copy = marker_image.copy()
        cv2.watershed(messi_ronaldo, marker_image_copy)
        
        segments = np.zeros(messi_ronaldo.shape,dtype=np.uint8)
        
        for color_ind in range(n_markers):
            segments[marker_image_copy == (color_ind)] = colors[color_ind]
        
        marks_updated = False
        
cv2.destroyAllWindows()