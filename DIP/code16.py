#PERFORM SUBTRACTION BY ADDING UNIT VALUE TO AN IMAGE

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img=Image.open('tiger1.jpg')

#convert image into numpy array
arr=np.array(img).astype(np.uint16)

#subtract constant value
result=arr-50

#keep pixel values between 0 and 255
result=np.clip(result, 0, 255)

#convert array into image
output=Image.fromarray(result.astype(np.uint8))

#Display original image
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

#Display brightened image
plt.subplot(1, 2, 2)
plt.imshow(output)
plt.title('Result Image')

plt.tight_layout()
plt.show()