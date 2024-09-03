import cv2
import numpy as np

# img=cv2.imread("/Users/ayushmishra/Desktop/OpenCV/multiimage.jpg")

# while True:
#     hsv=cv2.cvtColor(img,cv2.COLOR_BRG2HSV)
#     uv=np.array([247,89,89])
#     lv=np.array([122,47,47])

#     mask=cv2.inRange(hsv,lv,uv)


# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Load the image
image = cv2.imread('/Users/ayushmishra/Desktop/OpenCV/multiimage.jpg')

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range of the color red in HSV
# Lower and upper bounds of red color in HSV
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# Create masks for the red color
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
mask = mask1 | mask2

# Bitwise-AND mask and original image
result = cv2.bitwise_and(image, image, mask=mask)

# Display the original image and the result
cv2.imshow('Original Image', image)
cv2.imshow('Red Color Detection', result)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
