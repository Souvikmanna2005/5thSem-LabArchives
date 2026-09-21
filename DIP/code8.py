#show the intensity value of each pixel in an image

from PIL import Image
import numpy as np

#Open image and convert to grayscale
img = Image.open(r'C:\Users\SOUVIK MANNA\5th SEM\DIP\image1.jpg').convert('L')


#Convert image to numpy array
pixels=np.array(img)

#Print the intensity value of each pixel
print(pixels)