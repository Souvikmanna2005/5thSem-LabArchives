from PIL import Image

img=Image.open('image11.jpg')
print('Total number of pixel of original image:',img.size)

resized_image=img.resize((400,200))

resized_image.show()
print('Image resized successfully')