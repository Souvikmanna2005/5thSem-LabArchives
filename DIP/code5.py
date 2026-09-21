#rotate an image using PIL
from PIL import Image

image=Image.open(r'C:\Users\SOUVIK MANNA\5th SEM\DIP\image3.jpeg')

rotated=image.rotate(-45)
rotated.save("rotated.jpg")
rotated.show()
print("Image rotated successfully.")