import cv2 
import numpy as np
#python3 imageprocessing.py
img1=cv2.imread("/Users/ayushmishra/Desktop/OpenCV/WhatsApp Image 2024-08-20 at 21.33.jpeg",1)# if we change it to 0 the it shows black and white
# print(img1)
new_width = 800
new_height = 600
resized_image = cv2.resize(img1, (new_width, new_height))

cv2.imshow("original",img1)
cv2.imwrite()#save file
cv2.waitKey(0)
cv2.destroyAllWindows()  



