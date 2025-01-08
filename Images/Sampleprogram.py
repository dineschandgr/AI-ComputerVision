# Python program to explain cv2.imread() method 

# importing cv2 
import cv2 

# path 
path = r'img1.png'

# Using cv2.imread() method 
# Using 0 to read image in grayscale mode 
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 

# Displaying the image 
cv2.imshow('image', img) 

# Add a loop to handle GUI events
while True:
    key = cv2.waitKey(1) & 0xFF  # Wait for 1 ms
    if key == ord('q') or cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) < 1:
        break

# Destroy all OpenCV windows
cv2.destroyAllWindows()