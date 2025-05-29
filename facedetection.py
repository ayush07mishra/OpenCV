import cv2

image = cv2.imread('/Users/ayushmishra/Desktop/OpenCV/WhatsApp Image 2024-08-20 at 21.33.24.jpeg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)#convert to greay


#predefine face recognization file...
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces = face_cascade.detectMultiScale(gray_image,1.5,2)#use to detect using cascade


# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 4)



# Display the output image
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()




