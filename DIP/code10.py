#convert an image from rgb to binary

from PIL import Image

#open rgb image
img = Image.open(r'C:\Users\SOUVIK MANNA\5th SEM\DIP\image3.jpeg')

#convert rgb image to grayscale
gray_img = img.convert('L')

#set threshold value
threshold = 128

#convert grayscale image to binary using threshold
binary_img = gray_img.point(lambda x: 255 if x > threshold else 0)

#Display the binary image
binary_img.show()

#save the binary image
binary_img.save("binary_image.jpg")