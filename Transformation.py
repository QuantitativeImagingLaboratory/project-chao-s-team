import cv2
import numpy as np
import HistEqualization as equal
import io
import base64

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

    def compute_histogram_color(self,image):
        assert(len(image.shape)==3)
        if image.dtype != 'uint8':
            image=cv2.convertScaleAbs(image)
        hists=[]
        histR = [0]*256
        histG = [0]*256
        histB = [0]*256
        #get image dimensions 
        row,col=image.shape[0:2]
        for i in range(row):
            for j in range(col):
                histR[image[i,j][0]] = histR[image[i,j][0]] + 1
    
        for i in range(row):
            for j in range(col):
                histG[image[i,j][1]] = histG[image[i,j][1]] + 1

        for i in range(row):
            for j in range(col):
                histB[image[i,j][2]]= histB[image[i,j][2]] + 1
        hists.append(histR)
        hists.append(histG)
        hists.append(histB)
        return hists
        


    def adjust_gamma(self,image, gamma):
        # build a lookup table mapping the pixel values [0, 255] to
        # their adjusted gamma values
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255 
            for i in np.arange(0, 256)]).astype("uint8")
        # apply gamma correction using the lookup table              
        return cv2.LUT(image, table)

    def histogram_equalization(self, image):
        eq = equal.Histogram_Equalization()
        image = np.uint8(image)

        # print(image)
        flat_image = eq.hist_equalization(image)
        return flat_image

    def histogram_equalization_normalize(self,image):
        eq = equal.Histogram_Equalization()
        image = np.uint8(image)
        hist=eq.compute_histogram(image)
        norm_hist=eq.normalize_histogram(hist,image)
        return norm_hist

    def histogram_equalization_cumulative(self,image):
        eq = equal.Histogram_Equalization()
        hist=self.histogram_equalization_normalize(image)
        cum_hist=eq.cumulative_histogram(hist)
        return cum_hist

    def histogram_equalization_color(self, image):
        eq = equal.Histogram_Equalization()
        # if image is grayscale
        if len(image.shape) < 3:
            image = np.uint8(image)
            flat_image = eq.hist_equalization(image)
        else:
            # if image is colored:
            print("color")
            y_cr_cb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
            y, cr, cb = cv2.split(y_cr_cb)
            image = np.uint8(y)
            flat_image = eq.hist_equalization(image)
            img_back = cv2.merge((flat_image, cr, cb))
            flat_image = cv2.cvtColor(img_back, cv2.COLOR_YCrCb2BGR)
        return flat_image



    def negative(self,image):

        return 255-image

    def log(self,image):
        c=255/(np.log(1+255))
        image.astype(float)
        image=g = c*(np.log(1 + image))
        return image.astype(np.uint8)

    def histmatch(self,originalImage, referenceImage):
        values_int= 255
        if len(originalImage.shape) < 3:
            originalImage = originalImage[:,:,np.newaxis]
            referenceImage = referenceImage[:,:,np.newaxis]
        resultantImage = originalImage.copy()
        for d in range(originalImage.shape[2]):
            srcimage,bins = np.histogram(originalImage[:,:,d].flatten(),values_int,normed=True)
            destimage,bins = np.histogram(referenceImage[:,:,d].flatten(),values_int,normed=True)
            value_cdf_src  = srcimage.cumsum()
            value_cdf_src = (255 * value_cdf_src / value_cdf_src[-1]).astype(np.uint8)
            value_cdf_dest  = destimage.cumsum()
            value_cdf_dest = (255 * value_cdf_dest / value_cdf_dest[-1]).astype(np.uint8)
            image2  = np.interp(originalImage[:,:,d].flatten(),bins[:-1],value_cdf_src)
            image3  = np.interp(image2,value_cdf_dest, bins[:-1])
            resultantImage[:,:,d] = image3.reshape((originalImage.shape[0],originalImage.shape[1] ))
        return resultantImage
        

