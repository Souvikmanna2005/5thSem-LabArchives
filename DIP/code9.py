#convert RGB image to grayscale
from PIL import Image

#Open RGB image
img = Image.open(r'C:\Users\SOUVIK MANNA\5th SEM\DIP\image6.jpeg')

#convert to grayscale
gray_img = img.convert('L')

#Display the grayscale image
gray_img.show()

#save the grayscale image
gray_img.save("grayscale_image.jpg")