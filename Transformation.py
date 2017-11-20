import cv2
import numpy as np
from HistEqualization import Histogram_Equalization

class Transformation(object):
    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""
        #create empty array
        hist = [0]*256
        #get image dimensions 
        row,col=image.shape[0:2]
        #count pixels for each intensity level
        for i in range(row):
            for j in range(col):
                hist[image[i,j]] = hist[image[i,j]] + 1
        return hist

    def adjust_gamma(self,image, gamma):
        # build a lookup table mapping the pixel values [0, 255] to
        # their adjusted gamma values
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255 
            for i in np.arange(0, 256)]).astype("uint8")
        # apply gamma correction using the lookup table              
        return cv2.LUT(image, table)

    def histogram_equalization(self, image):

        eq = Histogram_Equalization()
        image = np.uint8(image)

        # print(image)
        flat_image = eq.hist_equalization(image)

        return flat_image



"""
original = cv2.imread("lena512.bmp",0)
adjusted = Transformation.adjust_gamma(original, gamma=3)
cv2.imshow("Images",adjusted)
cv2.waitKey(0)
"""