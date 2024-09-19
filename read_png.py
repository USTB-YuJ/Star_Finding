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

if __name__ == "__main__":
    image_ori = cv2.imread('./png_data/14.png', 1)
    sobel_result = sobel_(image_ori)
    cv2.imwrite("./sobel_data/14.png", sobel_result)

