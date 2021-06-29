import numpy as numpy
import cv2
import matplotlib.pyplot as pyplot

def canny() :
    img = cv2.imread('./original/straight01.png', cv2.IMREAD_GRAYSCALE)
    #img = cv2.imread('./orignial/rightCurve01.jpg', cv2.IMREAD_GRAYSCALE)

    edge1_th = [50, 200]
    edge2_th = [100, 200]
    edge3_th = [120, 200]

    edge1 = cv2.Canny(img, edge1_th[0], edge1_th[1])
    edge2 = cv2.Canny(img, edge2_th[0], edge2_th[1])
    edge3 = cv2.Canny(img, edge3_th[0], edge3_th[1])

    cv2.imshow('original', img)
    cv2.imshow('Low : ' + str(edge1_th[0]) + ', High : ' + str(edge1_th[1]), edge1)
    cv2.imshow('Low : ' + str(edge2_th[0]) + ', High : ' + str(edge2_th[1]), edge2)
    cv2.imshow('Low : ' + str(edge3_th[0]) + ', High : ' + str(edge3_th[1]), edge3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

canny()
