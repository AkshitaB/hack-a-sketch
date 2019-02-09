import cv2

class Stroker(object):

    def __init__(self):
        pass

    def create_tmp_file_name(self):
        pass

    def detect_edges(self, path):
        img = cv2.imread(path, 0)
        edges = cv2.Canny(img, 100, 200)
        return edges

    def rank_strokes(edges):
        pass