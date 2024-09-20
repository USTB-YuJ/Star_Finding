#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName: read_npy.py
# @Time : 2024/9/19 22:55
# @Author : USTB_YuJia
'''
此文件打开存储的npy文件，进行初步的数据分析以及二值化可视化。
'''
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pylab as plt2

def calculate_num(data):
    # 取99.992%处的值作为阈值，进行二值化
    p9_value = np.percentile(data, 99.992)
    result = np.sum(data > p9_value)
    return p9_value, result
def draw_bins(data):
    # 绘制直方图
    n, bins, patche = plt.hist(data, bins=100, range=(data.min(), data.max()), edgecolor='black', rwidth=0.8, log=True)  # bins参数控制直方图的条形数量
    plt.axvline(np.mean(data), color='r', linestyle='dashed', linewidth=2, label='Mean')
    print("mean(data) = ", np.mean(data))
    # plt.axvline(np.median(data), color='g', linestyle='dashed', linewidth=2, label='Median')
    plt.title('Data Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

def draw_3d(data):

    # 创建一个图形和一个3D子图
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # 获取数组的x, y坐标
    x, y = np.meshgrid(np.arange(data.shape[0]), np.arange(data.shape[1]))
    # 绘制三维曲面图
    surf = ax.plot_surface(x, y, data, cmap='viridis')
    # 添加颜色条
    fig.colorbar(surf)
    # 设置标签
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Value')
    # 显示图形
    plt.show()

def thres_(data,threshold):

    # 使用条件表达式来置值
    data[data > threshold] = 255
    data[data <= threshold] = 0

if __name__ == "__main__":
    # 设置.npy文件的路径
    npy_file_path = './npy_data/7.npy'
    # 加载.npy文件
    data = np.load(npy_file_path)
    data = data.astype(np.float32)
    # print("数组内容：")
    print("data.min() = ", data.min())
    print("data.max() = ", data.max())
    print("data.var() = ", np.var(data))
    print("data.mean() = ", np.mean(data))
    # draw_3d()
    # draw_bins(data)
    thres, num = calculate_num(data)
    print("阈值=", thres)
    thres_(data, thres)
    plt2.imshow(data)
    plt2.show()
