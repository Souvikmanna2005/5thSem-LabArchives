#crop an image

import cv2

image=cv2.imread(r'C:\Users\SOUVIK MANNA\5th SEM\DIP\image2.jpeg')

#check if image is loaded
if image is None:
    print("Error:image not found.")
    exit()

#crop the image
#format: image[y1:y2, x1:x2]
cropped=image[100:400, 150:450]

#display ORIGINAL & cropped image
cv2.imshow('Original image',image)
cv2.imshow('Cropped image',cropped)

#SAVE cropped image
cv2.imwrite('cropped_image.jpg',cropped)

cv2.waitKey(0)