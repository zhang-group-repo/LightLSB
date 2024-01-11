import os
from skimage import io, img_as_ubyte
import cv2
from skimage.metrics import peak_signal_noise_ratio
from skimage.util import img_as_ubyte
from PIL import Image
import numpy as np
from collections import Counter
from skimage import img_as_ubyte, color
import matplotlib.pyplot as plt
from skimage.io import imsave

# 改进后的无扩展有意义是5 10 1
def block_no_expand(name):
    """
    改进后的有意义加密
    :param name:
    :return:
    """
    im=np.array(Image.open(name))
    im_lab=cv2.cvtColor(im,cv2.COLOR_RGB2HSV)
    im_lab[:,:,-1]=np.interp(im_lab[:,:,-1],(0,255),(0,255/4))
    im_rgb=cv2.cvtColor(im_lab,cv2.COLOR_HSV2RGB)
    im_ht=Image.fromarray(im_rgb).convert("1")
    im_ht=img_as_ubyte(im_ht)
    # gray_level(im_ht,(2,4),True)
    return im_ht

if __name__ == '__main__':
    path = r"Aaron_Patterson_0001.jpg"#需要加密的图
    share = block_no_expand(path)

    # 将PIL Image对象转换为NumPy数组，以便使用cv2.imshow
    share_np = np.array(share)
    img = np.array(Image.open(path))

    # 显示多张图像
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(share_np, cmap='gray')
    plt.title('Merged Picture')

    plt.show()