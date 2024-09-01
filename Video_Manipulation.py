# import cv2
# #python3 Video_Manipulation.py
# video=cv2.VideoCapture("/Users/ayushmishra/Desktop/OpenCV/IMG_2185.MOV")

# while True:
#     ret,frame=video.read()
#     frame=cv2.resize(frame(700,450))
#     cv2.imshow("frame",frame)
#     k=cv2.waitKey(25)
#     if k==ord('f')& 0XFF:
#         break
# video.release()
# cv2.destroyAllWindows()  
import cv2

# Open a video file or capture device
cap = cv2.VideoCapture(0)  # Use 0 for webcam or provide video file path

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Check if the frame is read correctly
    if not ret:
        print("Failed to grab frame")
        break

    # Resize the frame
    resized_frame = cv2.resize(frame, (700, 450))  # (width, height)

    # Display the resized frame
    cv2.imshow('Resized Frame', resized_frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
