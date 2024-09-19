import cv2
import math
import matplotlib.pyplot as plt
import numpy as np

def contour_detec(image,data,data_thres):
    # 寻找轮廓
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(gray_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    npy_part_list = []
    # 遍历每个轮廓
    for contour in contours:
        # 计算轮廓的面积
        area = cv2.contourArea(contour)

        # 计算轮廓的周长
        perimeter = cv2.arcLength(contour, True)

        # 计算包围框
        x, y, w, h = cv2.boundingRect(contour)
        # 绘制包围框
        # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # 截取npy数组中的原光子数
        npy_part = cut_npy(data, x, y, w, h)
        npy_part_list.append(npy_part)
        # print(npy_part)
        # 找出最大值
        lightest_ = np.max(npy_part)
        if lightest_ < data_thres:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), -1)
        # print(lightest_)
        # 保存图像
        cv2.imwrite('./clear/5.jpg', image)
    return npy_part_list

def cut_npy(npy_data,x,y,w,h):
    # 计算起始坐标
    start_x = max(x - 1, 0)
    start_y = max(y - 1, 0)

    # 计算结束坐标
    end_x = min(x + w + 1, len(npy_data[0]))
    end_y = min(y + h + 1, len(npy_data[1]))

    # 进行切片
    return [row[start_x:end_x] for row in npy_data[start_y:end_y]]

def circle_checking(area, perimeter,contour,image):
    # 打印面积和周长
    print(f"Area: {area}, Perimeter: {perimeter}")

    # 可以根据面积和周长进一步判断轮廓是否为圆形
    # 例如，计算形状因子 (4 * π * 面积 / 周长的平方)
    shape_factor = (4 * math.pi * area) / (perimeter ** 2)
    print(f"Shape Factor: {shape_factor}")

    if shape_factor > 0.8:  # 判定为圆形
        cv2.drawContours(image, contour, -1, (0, 255, 0), 3)
    else:
        cv2.drawContours(image, contour, -1, (0, 0, 255), 3)

if __name__ == '__main__':
    # 读取图像
    image = cv2.imread("./sobel_data/5.png", 1)
    npy_file_path = './npy_data/5.npy'
    data = np.load(npy_file_path)
    # 计算标准差以及均值
    std_deviation = np.std(data)
    data_mean = np.mean(data)
    data_threshold = data_mean + 5 * std_deviation
    print(data_threshold)
    npy_list = contour_detec(image, data, data_threshold)



    # 显示结果
    # plt.figure(figsize=(10, 8))
    # plt.subplot(231), plt.imshow(npy_list[6]), plt.title('npy_list[6]')
    # plt.subplot(232), plt.imshow(npy_list[7]), plt.title('npy_list[7]')
    # plt.subplot(233), plt.imshow(npy_list[8]), plt.title('npy_list[8]')
    # plt.subplot(234), plt.imshow(npy_list[9]), plt.title('npy_list[9]')
    # plt.subplot(235), plt.imshow(npy_list[10]), plt.title('npy_list[10]')
    # plt.subplot(236), plt.imshow(npy_list[11]), plt.title('npy_list[11]')
    # plt.show()
    # print(np.shape(gray_image))
