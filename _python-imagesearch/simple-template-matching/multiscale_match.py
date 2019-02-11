# USAGE
# python match.py --template cod_logo.png --images images

# import the necessary packages
import time

import numpy as np
import argparse
import imutils
import glob
import cv2
import pyautogui

# loop over the images to find the template in
def find_scaled_image (image):
    # load the image, convert it to grayscale, and initialize the
    # bookkeeping variable to keep track of the matched region
    # image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    found = None

    # loop over the scales of the image
    for scale in np.linspace(0.2, 2.0, 20)[::-1]:
        # resize the image according to the scale, and keep track
        # of the ratio of the resizing
        resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])

        # if the resized image is smaller than the template, then break
        # from the loop
        if resized.shape[0] < tH or resized.shape[1] < tW:
            break

        # detect edges in the resized, grayscale image and apply template
        # matching to find the template in the image
        # edged = cv2.Canny(resized, 50, 200)
        edged = resized.copy()
        result = cv2.matchTemplate(edged, template, cv2.TM_CCORR_NORMED)

        # TM_CCOEFF_NORMED for color images
        # TM_CCORR_NORMED for edged images ()
        # NORMED ~ [0,1] values

        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
        corr = result
        print ("corr",maxVal)
        print("ratio:", scale)
        # check to see if the iteration should be visualized

        # draw a bounding box around the detected region
        clone = np.dstack([edged, edged, edged])

        cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
            (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
        cv2.imshow("Visualize", clone)
        # cv2.waitKey(0)
        # time.sleep(1)

        # if we have found a new maximum correlation value, then ipdate
        # the bookkeeping variable
        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)
    return found

def find_in_image (image, scale):
    # load the image, convert it to grayscale, and initialize the
    # bookkeeping variable to keep track of the matched region
    # image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    found = None

    # loop over the scales of the image
    # resize the image according to the scale, and keep track
    # of the ratio of the resizing
    resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
    r = gray.shape[1] / float(resized.shape[1])

    # if the resized image is smaller than the template, then break
    # from the loop
    # if resized.shape[0] < tH or resized.shape[1] < tW:
    #     break

    # detect edges in the resized, grayscale image and apply template
    # matching to find the template in the image
    # edged = cv2.Canny(resized, 50, 200)
    edged = resized.copy()
    result = cv2.matchTemplate(edged, template, cv2.TM_CCORR_NORMED)

    # TM_CCOEFF_NORMED for color images
    # TM_CCORR_NORMED for edged images ()
    # NORMED ~ [0,1] values

    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
    corr = result
    print ("corr",maxVal)
    print("ratio:", scale)
    # check to see if the iteration should be visualized

    # draw a bounding box around the detected region
    clone = np.dstack([edged, edged, edged])

    cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
        (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
    cv2.imshow("Visualize", clone)
    # cv2.waitKey(0)
    # time.sleep(1)

    # if we have found a new maximum correlation value, then ipdate
    # the bookkeeping variable
    if found is None or maxVal > found[0]:
        found = (maxVal, maxLoc, r)
    return found




# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-t", "--template", required=True, help="Path to template image")
# ap.add_argument("-i", "--images", required=True,
# 	help="Path to images where template will be matched")
# ap.add_argument("-v", "--visualize",
# 	help="Flag indicating whether or not to visualize each iteration")
# args = vars(ap.parse_args())
#
# # load the image image, convert it to grayscale, and detect edges
# template = cv2.imread(args["template"])


# template = cv2.imread ("templates/logo_chrome.png")
template = cv2.imread ("templates/chrome.bmp")
# image = cv2.imread("templates/Screenshot.png")

image = pyautogui.screenshot()
image = np.array(image.getdata(), dtype='uint8') \
        .reshape((image.size[1], image.size[0], 3))



template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
# template = cv2.Canny(template, 50, 200)
(tH, tW) = template.shape[:2]
cv2.imshow("Template", template)

found = find_scaled_image(image)

print (found)
#
# # unpack the bookkeeping varaible and compute the (x, y) coordinates
# # of the bounding box based on the resized ratio
(maxCorr, maxLoc, r) = found

if maxCorr < 0.8:
    print ("Image not found")

if (len(found) > 0 ) :
    (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
    (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
    loc = ( (startX + endX)/2, (startY+endY)/2 )

    # # draw a bounding box around the detected result and display the image
    # cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)

    # print (found)

    # loc = pyautogui.center(found)
    # pyautogui.rightClick(loc)
    pyautogui.click(loc)


# template = cv2.imread ("templates/logo_taskmgr.png")
# found = find_in_image(image, r)
#
# print (found)
# #
# # # unpack the bookkeeping varaible and compute the (x, y) coordinates
# # # of the bounding box based on the resized ratio
# (maxCorr, maxLoc, r) = found
#
# if maxCorr < 0.8:
#     print ("Image not found")
#
# if (len(found) > 0 ) :
#     (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
#     (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
#     loc = ((startX + endX)/2, (startY+endY)/2 )
#
#     # # draw a bounding box around the detected result and display the image
#     # cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
#     # cv2.imshow("Image", image)
#     # cv2.waitKey(0)
#
#     # print (found)
#
#     # loc = pyautogui.center(found)
#     # pyautogui.rightClick(loc)
#     pyautogui.click(loc)


print ( " END OF PROGRAM ")

cv2.waitKey(0)
cv2.destroyAllWindows()