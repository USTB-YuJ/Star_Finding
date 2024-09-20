#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName: read_fits.py
# @Time : 2024/9/19 22:55
# @Author : USTB_YuJia
'''
打开fits文件，观察header中的信息，并进行初步图像观察
'''
from astropy.io import fits
import pylab as plt
import os

path = '../fit_datasets/20240306204815059_6002.fits'
hdulist = fits.open(path, mode='update', output_verify='fix')
header = hdulist[0].header
data = hdulist[0].data

hdulist.info()

for key in header:
    print(key, header[key])


plt.imshow(data)
plt.colorbar()
plt.show()

# folder_path = '../fit_datasets/'
# idx = 0
# for root, dirs, files in os.walk(folder_path):
#     for filename in files:
#         file_path = os.path.join(root, filename)
#         print(file_path)
#         hdulist = fits.open(file_path, mode='update', output_verify='fix')
#         header = hdulist[0].header
#         # 读取EXPOSURE值
#         exposure_time = header['EXPOSURE']
#
#         # 打印EXPOSURE值
#         print('{},EXPOSURE={}'.format(idx, exposure_time))
#         idx = idx + 1