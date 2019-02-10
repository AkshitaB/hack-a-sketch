import math

import cv2
import numpy as np


def split_item(item, thresh):
    items = []
    length = len(item)
    if length > thresh:
        num_new_items = math.ceil(length/thresh)
        print(num_new_items)
        start = 0
        for i in range(num_new_items):
            end = start+thresh
            if end > length:
                end = length
            items.append(item[start:end])
            start = start + thresh
    return items

class Stroker(object):

    def __init__(self):
        pass

    def create_tmp_file_name(self):
        pass

    def detect_edges(self, path):
        img = cv2.imread(path)
        img = cv2.resize(im, (700, 700))

        imCopy = np.zeros(im.shape)
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        image, contours, hierarchy =  cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours]

        new_contours = []
        #for cont in contours:
        #    new_contours = new_contours + split_item(cont, 10)
            
        #contours = new_contours

        contours = np.array(sorted(contours, key=len, reverse=True))
        return contours

