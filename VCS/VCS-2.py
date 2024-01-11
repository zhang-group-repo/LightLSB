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

def basic_rg_vcs(img_name="lena.png", n=10):
    img_arr = np.invert(Image.open(img_name).convert("1"))
    shares = np.zeros((n,)+img_arr.shape, bool)
    for (i, j), p in np.ndenumerate(img_arr):
        if p:
            for ind in range(n):
                shares[ind, i, j] = np.random.choice([True, False])
        else:
            v = np.random.choice([True, False])
            shares[:, i, j] = v
    return shares

if __name__ == '__main__':
    shares = basic_rg_vcs(r"Aaron_Eckhart_0001.jpg" )
    share = shares[0]
    for i in range(1,len(shares)):
        share = share & shares[i]
    Image.fromarray(share).show()
