#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName: png2sobel.py
# @Time : 2024/9/19 22:55
# @Author : USTB_YuJia
'''
此文件读入png图像进行sobel算子处理，进行可视化，并将结果存储。
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

def sobel_(data):
    # 应用Sobel算子
    sobelx = cv2.Sobel(data, cv2.CV_64F, 1, 0, ksize=9)  # x方向
    sobely = cv2.Sobel(data, cv2.CV_64F, 0, 1, ksize=9)  # y方向

    # 计算梯度幅度
    sobel = np.sqrt(sobelx ** 2 + sobely ** 2)

    # # 显示结果
    # plt.figure(figsize=(10, 8))
    # plt.subplot(141), plt.imshow(data, cmap='gray'), plt.title('Original Image')
    # plt.subplot(142), plt.imshow(sobelx, cmap='gray'), plt.title('Sobel X')
    # plt.subplot(143), plt.imshow(sobely, cmap='gray'), plt.title('Sobel Y')
    # plt.subplot(144), plt.imshow(sobel, cmap='gray'), plt.title('Sobel')
    # plt.show()

    return sobel

if __name__ == "__main__":
    image_ori = cv2.imread('./mess/13_ad.png', 1)
    sobel_result = sobel_(image_ori)
    cv2.imwrite("./sobel_data_ad/13.png", sobel_result)