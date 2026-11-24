#Division of two grayscale images using unique integers 
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Read two grayscale images
img=Image.open("tiger1.jpg").convert("L")

arr=np.array(img).astype(np.uint16)

#Divide by constant value
result=arr/2

#Keep pixel values within 0 to 255
result=np.clip(result,0,255)
output=Image.fromarray(result.astype(np.uint8))

#Display original Image
plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.title('Original Image')
plt.axis('off')

#Display result Image
plt.subplot(1,2,2)
plt.imshow(result,cmap='gray')
plt.title('Result Image')
plt.axis('off')

plt.tight_layout()
plt.show()