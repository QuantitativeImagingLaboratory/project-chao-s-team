import numpy as np
import cv2
import base64
from PIL import Image
import io

def histmatch(originalImage, referenceImage):
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


original = cv2.imread("Lenna.png")
math=cv2.imread('Lenna0.jpg')
adjusted = histmatch(original,math)
cv2.imshow("Images",adjusted)
cv2.waitKey(0)
