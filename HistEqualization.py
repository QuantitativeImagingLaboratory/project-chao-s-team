__author__ = "Gauri Bulbule"
import numpy as np
import cv2
import matplotlib.pyplot as plt

class Histogram_Equalization:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""
        [x, y] = image.shape
        hist = [0] * 256
        for i in range(0, x):
            for j in range(0, y):
                intensity = image[i, j]
                hist[intensity] = hist[intensity] + 1

        return hist

    def normalize_histogram(self, hist, image):
        #normalize the histogram
        #k=256
        [x, y] = image.shape
        norm_hist = np.array(hist)/(x*y)

        return norm_hist


    def cumulative_histogram(self, norm_hist):

        # finds cumulative sum of a numpy array, list
        cumulative_hist = norm_hist
        x = len(cumulative_hist)
        sum = 0
        for i in range(0, x):
            sum = sum + cumulative_hist[i]
            cumulative_hist[i] = sum

        return cumulative_hist


    def compute_intermediate_imageJ1(self, image, cumulative_hist):
        x, y = image.shape
        image_J1 = np.zeros((x,y))

        for i in range(0, x):
            for j in range(0, y):
                value = image[i,j]
                image_J1[i,j] = cumulative_hist[value]

        return image_J1


    def compute_flattened_image(self, image_J1):

        x, y = image_J1.shape
        flattened_image = np.zeros((x, y),np.uint8)
        K = 256 - 1  # k-1

        for i in range(0, x):
            for j in range(0, y):
                flattened_image[i, j] = int((K) * image_J1[i, j] + 0.5)

        return flattened_image


    def hist_equalization(self, image):

        hist = self.compute_histogram(image)
        #plt.figure(1)
        #hist_fig = plt.plot(hist)
        #plt.savefig("hist_original_image.png")

        normalized_hist = self.normalize_histogram(hist, image)
        cumulative_hist = self.cumulative_histogram(normalized_hist)
        intermediate_image = self.compute_intermediate_imageJ1(image, cumulative_hist)
        flattened_image = self.compute_flattened_image(intermediate_image)

        #hist2 = self.compute_histogram(flattened_image)
        #plt.figure(2)
        #hist_fig2 = plt.plot(hist2)
        #plt.savefig("hist_flattened_image.png")

        return flattened_image


