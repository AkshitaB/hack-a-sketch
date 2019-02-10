import math

import cv2
import numpy as np


def split_item(item, thresh):
    items = []
    length = len(item)
    if length == 1:
        return items
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
    else:
        items = [item]
    return items

class Stroker(object):

    def __init__(self):
        pass

    def create_tmp_file_name(self):
        pass

    def detect_edges(self, path):
        img = cv2.imread(path)
        img = cv2.resize(img, (700, 700))

        imCopy = np.zeros(img.shape)
        imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        image, contours, hierarchy =  cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

        contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours]

        

        contours = sorted(contours, key=len, reverse=True)
        #'''
        new_contours = []
        for cont in contours:
            new_contours = new_contours + split_item(cont, 20)
            
        contours = new_contours
        #'''

        contours = [contour.tolist() for contour in contours]
        
        contour_strings = []
        for contour in contours:
            st = 'm'
            for idx, x in enumerate(contour):
                if idx == 1:
                    st += ' L'
                st += ' {},{}'.format(x[0][0], x[0][1])
            contour_strings.append(st)
        return contour_strings
        
        #return contours
