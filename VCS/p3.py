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

def basic_single_vcs(img_name="lena.png", to_save=False):
    img_arr = halftone(img_name)
    share1 = np.random.choice([True, False], img_arr.shape)
    share2 = np.zeros_like(share1)
    for (i, j), p in np.ndenumerate(img_arr):
        if p:
            share2[i, j] = share1[i, j]
        else:
            share2[i, j] = not share1[i, j]
    if to_save:
        basename = os.path.splitext(img_name)[0]
        io.imsave("basic_single_vcs_share1_%s.png" % basename,
                  img_as_ubyte(share1))
        io.imsave("basic_single_vcs_share2_%s.png" % basename,
                  img_as_ubyte(share1))
        io.imsave("basic_single_vcs_decrypted_%s.png" % basename,
                  img_as_ubyte(share1 & share2))
    else:
        return share1, share2

if __name__ == '__main__':
    share1,share2 = basic_single_vcs(r"Aaron_Eckhart_0001.jpg" )
    share = (share1 & share2)
    Image.fromarray(share).show()
