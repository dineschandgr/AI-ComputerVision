import cv2
from cv2 import VideoCapture, imwrite, waitKey, destroyWindow, imshow
import matplotlib.pyplot as plt

cam_port = 0
cam = VideoCapture(cam_port)

# reading the input using the camera
result, image = cam.read()

# If image will detected without any error,
# show result

if result:
    # Convert BGR to RGB for Matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title("Captured Image")
    plt.axis("off")
    plt.show()

# If captured image is corrupted, moving to else part
else:
	print("No image detected. Please! try again")

imwrite("test2.png", image)