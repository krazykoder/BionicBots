# 
# Created by towshif ali (tali) on 2/5/2019
#

import numpy as np
import cv2


# Define image path
image_path = './coins_image.png'
# image_path = './watershed_coins_01.jpg'

def run_main():
    cap = cv2.imread(image_path)
    ## ignore explicits if not needed
    # cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
    # cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 720)

    # while(True):
    # ret, frame = cap.read()
    # roi = frame[0:500, 0:500]
    roi = cap.copy()
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
    # gray_blur = cv2.blur(gray, (15, 15), 0)

    thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 1)

    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,
    kernel, iterations=1)

    cont_img = closing.copy()
    contours, hierarchy = cv2.findContours(cont_img, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 2000 or area > 4000:
            continue

        if len(cnt) < 5:
            continue

        ellipse = cv2.fitEllipse(cnt)
        cv2.ellipse(roi, ellipse, (0,255,0), 2)

    cv2.imshow("Morphological Closing", closing)
    cv2.imshow("Adaptive Thresholding", thresh)
    cv2.imshow('Contours', roi)


    # wait for key press to exit
    if cv2.waitKey(0) & 0xFF == ord('q'):
        return

    # cap.release()
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    run_main()