#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName: main.py
# @Time : 2024/9/19 23:08
# @Author : USTB_YuJia
'''
此文件为集合全流程
'''
import math
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import numpy as np
#from astropy.utils.data import download_file
from astropy.io import fits
import cv2
import os

def normalize_to_255(arr):
    arr_max = arr.max()
    arr_nor = arr / arr_max
    arr_255 = (arr_nor*255).astype(np.uint8)
    return arr_255

def transform_fit(path):
    with fits.open(path, mode='update', output_verify='fix') as hdulist:
        header = hdulist[0].header
        data = hdulist[0].data

        hdulist.info()
        # np.save("./npy_data/" + str(name_id) + ".npy", data)

        image = normalize_to_255(data)
        cv2.imshow("png", image)
        cv2.waitKey(0)
        cv2.destroyWindow()

if __name__ == "__main__":
    transform_fit('../fit_datasets/20240306204816083_6002.fits')
