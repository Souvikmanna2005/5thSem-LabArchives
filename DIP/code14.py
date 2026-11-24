#DIVISION OF TWO GRAYSCALE IMAGE
from PIL import Image,ImageChops
import matplotlib.pyplot as plt
import numpy as np

#Read two grayscale images
img1=Image.open("tiger1.jpg").convert("L")
img2=Image.open("tiger2.jpg").convert("L")


#resize both images to same size
img2=img2.resize(img1.size)

#Convert images into NumPy arrays
arr1=np.array(img1).astype(np.float32)
arr2=np.array(img2).astype(np.float32)

#Avoid division by zero
arr2[arr2==0]=1

#Perform division
result=(arr1/arr2)*255

#Keep pixel values within 0 to 255
result=np.clip(result,0,255)

#Convert NumPy array into PIL Image
output=Image.fromarray(result.astype(np.uint8)) 

#Display Images
plt.figure(figsize=(12,4))

#Display Image1
plt.subplot(1,3,1)
plt.imshow(img1,cmap='gray')
plt.title('Image 1')
plt.axis('off')

#Display Image2
plt.subplot(1,3,2)
plt.imshow(img2,cmap='gray')
plt.title('Image 2')
plt.axis('off')

#Display Division Result
plt.subplot(1,3,3)
plt.imshow(result,cmap='gray')
plt.title('Division Result')
plt.axis('off')

plt.show()