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
        # for key in header:
            # print(key, header[key])

        # np.save("./npy_data/" + str(name_id) + ".npy", data)

        image = normalize_to_255(data)
        print(np.shape(image))
        cv2.imwrite("./png_data_2/" + str(name_id) + ".png", image)
        # print(image)

if __name__ == "__main__":

    folder_path = '../fit_datasets/'
    idx = 0

    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            print(file_path)
            transform_fit(file_path, idx)
            idx = idx + 1
