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

def basic_prob_vcs(img_name="lena.png", to_save=False):
    B0 = np.array([[1, 0], [1, 0]], bool)
    B1 = np.array([[0, 1], [1, 0]], bool)
    img_arr = halftone(img_name)
    share1 = np.zeros_like(img_arr, bool)
    share2 = np.zeros_like(img_arr, bool)
    for (i, j), p in np.ndenumerate(img_arr):
        if p:
            (share1[i, j], share2[i, j]) = B0[:, np.random.choice(B0.shape[1])]
        else:
            (share1[i, j], share2[i, j]) = B1[:, np.random.choice(B0.shape[1])]
    if to_save:
        io.imsave("basic_pvcs_decrypted_%s.png" % opath.splitext(img_name)[0],
                  img_as_ubyte(share1 & share2))
    else:
        return share1, share2

if __name__ == '__main__':
    share1,share2 = basic_prob_vcs(r"Aaron_Eckhart_0001.jpg" )
    share = (share1 & share2)
    Image.fromarray(share).show()
