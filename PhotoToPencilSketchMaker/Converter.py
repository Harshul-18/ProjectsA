import numpy as np      # pip install numpy
import imageio          # pip install imageio
import scipy.ndimage    # pip install scipy
import cv2              # pip install opencv

img = "Lena.png"

def rgb2gray(rgb):
    # Using the 2-dimensional array formula to convert image to gray scale
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

def toSketch(front, back):
    pencilSketch = (front * 255)/(255 - back)

    pencilSketch[pencilSketch>255] = 255
    pencilSketch[back==255] = 255

    return pencilSketch.astype("uint8")

# Reading the image
imgReader = imageio.imread(img) 

# Converting the image to gray scale (black and white)
grayImage = rgb2gray(imgReader)

# Converting the image into blur image
blurredImage = scipy.ndimage.filters.gaussian_filter(255-grayImage, sigma=15)

# Converting the image to pencil sketch using blurred and gray scale images
sketchedImage = toSketch(blurredImage, grayImage) 

cv2.imwrite("Lena(Sketch).png", sketchedImage)

