#SUBTRACTION OF TWO GRAYSCALE IMAGE

from PIL import Image, ImageChops
import matplotlib.pyplot as plt

#read two grayscale image
img1=Image.open('tiger1.jpg').convert('L')
img2=Image.open('tiger2.jpg').convert('L')

img2=img2.resize(img1.size)

#perform image addition
result=ImageChops.subtract(img1,img2)

#display image 1
plt.subplot(1, 3, 1)
plt.imshow(img1, cmap='gray')
plt.title('Image 1')
plt.axis('off')

#display image 2
plt.subplot(1, 3, 2)
plt.imshow(img2, cmap='gray')
plt.title('Image 2')
plt.axis('off')

#display Subtraction result
plt.subplot(1, 3, 3)
plt.imshow(result, cmap='gray')
plt.title('Subtraction Result')
plt.axis('off')

plt.show()