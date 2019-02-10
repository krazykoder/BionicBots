'''
Simple "Square Detector" program.
Loads several images sequentially and tries to find squares in each image.
'''

# Python 2/3 compatibility
import sys
PY3 = sys.version_info[0] == 3

if PY3:
    xrange = range

import numpy as np
import cv2 as cv
import imutils


def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def find_squares(img):
    img = cv.GaussianBlur(img, (5, 5), 0)
    cv.imshow('Blur', img)
    cv.waitKey(0)
    squares = []
    for gray in cv.split(img):
        for thrs in xrange(0, 255, 26):
            if thrs == 0:
                bin = cv.Canny(gray, 0, 50, apertureSize=5)
                bin = cv.dilate(bin, None)
                # cv.imshow('squares', bin)
                # cv.waitKey(0)
            else:
                _retval, bin = cv.threshold(gray, thrs, 255, cv.THRESH_BINARY)

            cv.imshow('Threshold', bin)
            cv.waitKey(0)

            contours = cv.findContours(bin, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
            contours = imutils.grab_contours(contours)
            contours = sorted(contours, key=cv.contourArea, reverse=True)[:5]

            # cv.drawContours(img, contours, -1, (0, 255, 0), 3)

            for cnt in contours:
                cnt_len = cv.arcLength(cnt, True)
                cnt = cv.approxPolyDP(cnt, 0.02*cnt_len, True)
                if len(cnt) == 4 and cv.contourArea(cnt) > 330 \
                        and cv.isContourConvex(cnt):
                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
                    if max_cos < 0.1:
                        squares.append(cnt)

    return squares

if __name__ == '__main__':
    from glob import glob
    # for fn in glob('calculatorUI.png'):
    # for fn in glob('winCalculator.bmp'):
    fn = 'calculatorUI.png'
    # fn = 'winCalculator.bmp'
    # fn = 'UIView.gif'
    img = cv.imread(fn)

    squares = find_squares(img)
    cv.drawContours( img, squares, -1, (0, 255, 0), 3 )
    cv.imshow('squares', img)
    cv.waitKey(0)
    cv.destroyAllWindows()