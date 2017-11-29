import numpy
import re
from PIL import Image

# open the image
# the tester image has 4 pixels
image = Image.open('testing-img.png')
# convert the image to an array using the numpy scientific package
image_array = numpy.array(image) # 640x480x4 array
# open the file
rgb_text_file = open("rgb-text-file.txt", "w")

# we will store 3 values for each pixel
# every pixel will represent one element in the list
# every pixel is represented by it's R, G and B values (RGB)
rgb_per_pixel = []

# iterate through the image array
# change the range according to the image size
for i in range(2):
	for j in range(2):
		# print R G B for the given pixel
		pixel_rgb = image_array[i,j]
		# editing
		pixel_rgb_modified = str(pixel_rgb).strip('[]')
		pixel_rgb_clean = re.sub(' +',' ', pixel_rgb_modified)
		rgb_per_pixel.append(pixel_rgb_clean)
		# print (pixel_rgb_clean)

# print the rgb_per_pixel list and write it to the defined file
for i in range(len(rgb_per_pixel)):
	rgb_text_file.write(rgb_per_pixel[i] + "\n")
	print(rgb_per_pixel[i])
	
rgb_text_file.close()
