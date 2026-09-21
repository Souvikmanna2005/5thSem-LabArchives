#flip an image horizontally and vertically using PIL
from PIL import Image

#open the image
img = Image.open(r'C:\Users\SOUVIK MANNA\5th SEM\DIP\image4.jpeg')

#horizontal flip
horizontal_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_flip.save("horizontal_flip.jpg")

#vertical flip
vertical_flip = img.transpose(Image.FLIP_TOP_BOTTOM)
vertical_flip.save("vertical_flip.jpg")

#Display the flipped images
horizontal_flip.show()
vertical_flip.show()

print("Image flipped horizontally and vertically successfully.")