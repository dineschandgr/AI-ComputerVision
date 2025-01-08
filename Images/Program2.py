import cv2
import numpy as np
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
img=cv2.imread("img1.png")
#Displaying image using plt.imshow() method
plt.imshow(img)

#hold the window
plt.waitforbuttonpress()
plt.close('all')