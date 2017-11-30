import numpy as np
import cv2
import base64
from PIL import Image
import io

def histogramMatching(image1, image2):
    image1 = b64toArray(image1)
    image2 =b64toArray(image2)
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

    return Arraytob64(resultImage)



def b64toArray(b64str):
	img = base64.b64decode(b64str)
	img = Image.open(io.BytesIO(img))
	return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

def Arraytob64(array):
	im = Image.fromarray(array.astype("uint8"))
	rawBytes = io.BytesIO()
	im.save(rawBytes, "JPEG")
	rawBytes.seek(0)  # return to the start of the file
	return base64.b64encode(rawBytes.read())