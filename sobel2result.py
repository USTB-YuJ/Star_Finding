#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @FileName: sobel2result.py
# @Time : 2024/9/19 22:55
# @Author : USTB_YuJia
'''
此文件为主要处理文件，进行多组处理方法，结果输出图像以及质心坐标
'''

import cv2
import math
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import math
def contour_detec(image_ori,npy_data,data_thres,id2save,ifsave:bool=False):
    # 寻找轮廓
    gray_image = cv2.cvtColor(image_ori, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(gray_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    npy_part_list = []
    lightmax_list = []
    coords_list = []
    # 遍历每个轮廓
    for contour in contours:

        # 计算包围框
        x, y, w, h = cv2.boundingRect(contour)

        # 绘制包围框
        # cv2.rectangle(image_ori, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # 截取npy数组中的原光子数
        npy_part = cut_npy(npy_data, x, y, w, h)
        npy_part_list.append(npy_part)
        # print(npy_part)
        # 找出最大值
        lightest_ = np.max(npy_part)
        lightmax_list.append(lightest_)
        # print(lightest_)

        # 判定光点的最大值是否在阈值之下
        if lightest_ < data_thres:
            cv2.rectangle(image_ori, (x, y), (x + w, y + h), (0, 0, 0), -1)
        # print(lightest_)
        else:
            # 计算星等
            magnitude = calculate_num_light(npy_part)
            cv2.putText(image, str(magnitude), (x+15,y+15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
            # 找到最大值的扁平索引
            flat_index = np.argmax(npy_part)
            # 将扁平索引转换为多维索引
            coords = np.unravel_index(flat_index, np.shape(npy_part))
            radius = int(((w / 2) ** 2 + (h / 2) ** 2) ** (1 / 2))
            coords_real = (x+coords[0], y+coords[1], radius)
            coords_list.append(coords_real)
            # 绘制圆
            cv2.circle(image_ori, (coords_real[0], coords_real[1]), radius, (0, 0, 255), 2)
    #保存图像
    if ifsave:
        cv2.imwrite('./clear_circled/'+str(id2save)+'.png', image_ori)
    return npy_part_list, lightmax_list, coords_list

def cut_npy(npy_data,x,y,w,h):
    # 计算起始坐标
    start_x = max(x - 1, 0)
    start_y = max(y - 1, 0)

    # 计算结束坐标
    end_x = min(x + w + 1, len(npy_data[0]))
    end_y = min(y + h + 1, len(npy_data[1]))

    # 进行切片
    return [row[start_x:end_x] for row in npy_data[start_y:end_y]]

def calculate_num_light(data_list):
    # 总光子数
    total_light = np.sum(data_list)
    # 光度 = 总光子数/曝光时间
    light_degree = total_light/28
    # 视星等 = 太阳视星等 - 2.5*lg(待测星光度/太阳光度)
    result = - 26.7 - 2.5*math.log10(light_degree/(3.827*10E26))
    return round(result,3)

def circle_checking(contour, img):
    # 计算轮廓的面积
    area = cv2.contourArea(contour)
    # 计算轮廓的周长
    perimeter = cv2.arcLength(contour, True)
    # 打印面积和周长
    print(f"Area: {area}, Perimeter: {perimeter}")
    # 计算形状因子 (4 * π * 面积 / 周长的平方)
    shape_factor = (4 * math.pi * area) / (perimeter ** 2)
    print(f"Shape Factor: {shape_factor}")

    if shape_factor > 0.8:  # 判定为圆形
        cv2.drawContours(img, contour, -1, (0, 255, 0), 3)
    else:
        cv2.drawContours(img, contour, -1, (0, 0, 255), 3)

def draw_figure(data4draw):
    plt.figure(figsize=(10, 10))
    plt.subplot(111), plt.imshow(data4draw), plt.title('title')
    plt.show()

def write_txt(list4write, txt_id, txt_path):
    with open(txt_path + str(txt_id) + ".txt", "w") as file:
        # 遍历数组的每一行
        for i, row in enumerate(list4write):
            # 将每一行的元素转换为字符串，并用空格分隔
            row_str = " ".join(map(str, row))
            # 写入行索引和行内容
            file.write(f"{row_str}\n")

if __name__ == '__main__':
    id_img = 0
    # for id_img in tqdm(range(0, 15)):
    # 读取图像
    image = cv2.imread("./sobel_data/"+str(id_img)+".png", 1)
    npy_file_path = './npy_data/'+str(id_img)+'.npy'
    data = np.load(npy_file_path)

    # 计算标准差以及均值
    std_deviation = np.std(data, ddof=0)
    data_mean = np.mean(data)
    data_threshold = data_mean + 8*std_deviation
    # print(data_threshold)

    npy_list, light_list, co_list = contour_detec(image, data, data_threshold, id_img, ifsave=True)

    write_txt(list4write=co_list, txt_id=id_img, txt_path="./center_txt/")


