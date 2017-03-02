'''
    Canny.py
    inf555

    - Converted to Python Source by Jinay Patel on 03/03/2017
    - Created by Camille MASSET on 18/11/2015.
    Copyright  2015 Basile Camille. All rights reserved.
'''
import cv2
import numpy as np


class CannyFilter:
    __low_threshold = 0
    __high_threshold = 0

    def __init__(self, low, high):
        self.__low_threshold = low
        self.__high_threshold = high

    def detectEdges(self, img):
        out = np.zeros((img.shape[:2]), dtype=img.dtype)
        gray = img.astype(dtype='uint8')

        edges = cv2.blur(gray, (3, 3))
        edges = cv2.Canny(edges, self.__low_threshold, self.__high_threshold, 3)

        # out = np.zeros(0)
        # np.copyto(out, img, where=edges)
        # plt.imshow(out, cmap='gray')
        # plt.show()
        return edges

    def get_thresholds(self):
        return self.__low_threshold, self.__high_threshold

if __name__ == '__main__':
    flt = CannyFilter(2, 2)
    print "thresholds (low, high): ", flt.get_thresholds()

    img = cv2.imread(
        "/home/jinay/workspace/git-repos/upwork/inf555/rapport/images/chaise-3d.png", 0)
    edges = flt.detectEdges(img)

    from matplotlib import pyplot as plt
    plt.imshow(edges, cmap='gray')
    plt.show()
