#resize an image using PIL
from PIL import Image

#open the image
image = Image.open(r'C:\Users\SOUVIK MANNA\5th SEM\DIP\image4.jpeg')

print("Total number of pixel of original image",image.size)

#resize the image
resized_image = image.resize((400, 200))

#save the resized image
resized_image.save("resized_image.jpg")

#show the resized image
resized_image.show()

print("Image resized successfully.")