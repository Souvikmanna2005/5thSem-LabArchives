#display height and width an image using PIL
from PIL import Image

img = Image.open('image1.jpg')
width, height = img.size

total_pixels = width * height

print("Width:", width)
print("Height:", height)
print("Total number of pixels:", total_pixels)