from skimage import io, img_as_ubyte
from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
import time

def halftone(img_name, convert_to_byte=True):
    img = Image.open(img_name)
    img = img.resize([i//2*2 for i in img.size])
    img_arr = np.array(img.convert("1"))
    if convert_to_byte:
        return img_as_ubyte(img_arr)
    return img_arr

def basic_vcs2(img_name="lena.png"):
    img_arr = halftone(img_name)
    share1 = np.zeros((img_arr.shape[0],2*img_arr.shape[1]),bool)
    share1[:][::2]=True
    share2 = np.zeros_like(share1)
    for (i, j), p in np.ndenumerate(img_arr):
            if p:
                share2[i, 2*j:2*(j+1)] = share1[i, 2*j:2*(j+1)]
            else:
                share2[i, 2*j:2*(j+1)] = np.invert(share1[i, 2*j:2*(j+1)])
    return share1, share2

if __name__ == '__main__':
    share1,share2 = basic_vcs2(r"Aaron_Eckhart_0001.jpg" )
    share = (share1 & share2)
    Image.fromarray(share).show()
