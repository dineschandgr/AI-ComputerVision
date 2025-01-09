import cv2

# Replace the URL with the IP Webcam/DroidCam video stream URL
# Example for IP Webcam: http://<IP>:<port>/video
camera_url = "http://192.168.29.200:4747/video"

# Open the video stream
cap = cv2.VideoCapture(camera_url)

if not cap.isOpened():
    print("Error: Cannot access the camera stream")
    exit()

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS)) if cap.get(cv2.CAP_PROP_FPS) > 0 else 20

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output-grey.mp4', fourcc, fps, (frame_width, frame_height), isColor=False)

while True:
    # Read frames from the camera
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to retrieve frame")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply edge detection using Canny
    edges = cv2.Canny(gray, 100, 200)

    # Display the original frame
    cv2.imshow("Original", frame)

    # Display the grayscale frame
    cv2.imshow("Grayscale", gray)

    # Display the edge-detected frame
    cv2.imshow("Edges", edges)

    cv2.imshow("Original1", frame)

    out.write(gray)

    # Press 'q' to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
out.release()
cv2.destroyAllWindows()
