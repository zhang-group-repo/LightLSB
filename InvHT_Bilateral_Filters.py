import cv2
import math, random
# import skimage
from skimage import io, img_as_ubyte
from skimage.util import view_as_blocks
from PIL import Image
import os
from os import path as opath
import matplotlib.pyplot as plt
import numpy as np

pre="lena"
path="lena_1_4.png"  # 需要逆半调的图
img=img_as_ubyte(Image.open(path))
pil_halftone = Image.open(path).convert('L').convert("1")
halftone = img_as_ubyte(pil_halftone)

orig_halftone_name="lena_ht.png"
orig_halftone=img_as_ubyte(io.imread(orig_halftone_name))

def IHT(radius=3,sigma_s=100,cnts=3):
    dehalftoned=halftone.copy()
    for i in range(cnts):
        dehalftoned = cv2.bilateralFilter(I,radius,sigma_s,sigma_s,dst=dehalftoned)
    return dehalftoned

for radius in range(1, 15,2): # 超参数
    for sigma_s in [10,20,30,50,100,150,200,400,500,600]: # 超参数
        for cnts in range(1,9): # 超参数
            I=cv2.GaussianBlur(halftone.copy(),(radius,radius),0)
            dehalftoned=IHT(radius,sigma_s,cnts)
            ehist=cv2.equalizeHist(dehalftoned) # ehist即为解密增强图像
            name=f"{pre}/{cnts}_{radius}_{sigma_s}.png"
            print("psnr:",name, peak_signal_noise_ratio(ehist,orig_halftone))
            rst=np.hstack([img,halftone,I,dehalftoned,ehist])
            cv2.imwrite(name,rst)