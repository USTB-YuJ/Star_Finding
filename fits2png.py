#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName: fits2png.py
# @Time : 2024/9/19 22:55
# @Author : USTB_YuJia
'''
此文件将fits文件打开，取出其中光子数组信息存储为npy文件，并且将其二值化处理存储为png文件。（阈值为手动设置）
'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#from astropy.utils.data import download_file
from astropy.io import fits
import cv2
import os

def normalize_to_255(arr):

    arr[arr > 50] = 255
    arr[arr < 50] = 0
    return arr

def transform_fit(path, name_id):
    with fits.open(path, mode='update', output_verify='fix') as hdulist:
        header = hdulist[0].header
        data = hdulist[0].data

        hdulist.info()
        np.save("./npy_data/" + str(name_id) + ".npy", data)

        image = normalize_to_255(data)
        cv2.imwrite("./png_data_2/" + str(name_id) + ".png", image)

if __name__ == "__main__":

    folder_path = '../fit_datasets/'
    idx = 0

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            print(file_path)
            transform_fit(file_path, idx)
            idx = idx + 1
