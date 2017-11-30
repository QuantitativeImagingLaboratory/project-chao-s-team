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


    def negative(self,image):
        return 255-image

    def log(self,image):
        c=255/(np.log(1+255))
        image.astype(float)
        image=g = c*(np.log(1 + image))
        return image.astype(np.uint8)


    def histogramMatching(self,image1, image2):
        image1 = self.b64toArray(image1)
        image2 = self.b64toArray(image2)
        values_int= 255
        if len(image1.shape) < 3:
            image1 = image1[:,:,np.newaxis]
            image2 = image2[:,:,np.newaxis]
        resultImage = image1.copy()
        for d in range(image1.shape[2]):
            srcimage,bins = np.histogram(image1[:,:,d].flatten(),values_int,normed=True)
            destimage,bins = np.histogram(image2[:,:,d].flatten(),values_int,normed=True)
            value_cdf_src  = srcimage.cumsum()
            value_cdf_src = (255 * value_cdf_src / value_cdf_src[-1]).astype(np.uint8)
            value_cdf_dest  = destimage.cumsum()
            value_cdf_dest = (255 * value_cdf_dest / value_cdf_dest[-1]).astype(np.uint8)
            image2  = np.interp(image1[:,:,d].flatten(),bins[:-1],value_cdf_src)
            image3  = np.interp(image2,value_cdf_dest, bins[:-1])
            resultImage[:,:,d] = image3.reshape((image1.shape[0], image1.shape[1] ))

        return self.Arraytob64(resultImage)



    def b64toArray(self,b64str):
        img = base64.b64decode(b64str)
        img = Image.open(io.BytesIO(img))
        return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

    def Arraytob64(self,array):
        im = Image.fromarray(array.astype("uint8"))
        rawBytes = io.BytesIO()
        im.save(rawBytes, "JPEG")
        rawBytes.seek(0)  # return to the start of the file
        return base64.b64encode(rawBytes.read())







"""
original = cv2.imread("lena512.bmp",0)
adjusted = Transformation.adjust_gamma(original, gamma=3)
cv2.imshow("Images",adjusted)
cv2.waitKey(0)
"""