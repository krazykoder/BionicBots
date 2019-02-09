# USAGE
# python match.py --template cod_logo.png --images images

# import the necessary packages
import numpy as np
import argparse
import imutils
import glob
import cv2
from PIL import ImageGrab
import PIL
import pyautogui

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--template", required=True, help="Path to template image")
ap.add_argument("-i", "--images", required=True,
	help="Path to images where template will be matched")
ap.add_argument("-v", "--visualize",
	help="Flag indicating whether or not to visualize each iteration")
args = vars(ap.parse_args())

# load the image image, convert it to grayscale, and detect edges
template = cv2.imread(args["template"])
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template = cv2.Canny(template, 50, 200)
(tH, tW) = template.shape[:2]
cv2.imshow("Template", template)

# get video feed from computer screen

# get video feed from cam
# cap = cv2.VideoCapture(0)

while(True):
    # img = ImageGrab.grab()
    # mywidth = 1200
    # wpercent = (mywidth / float(img.size[0]))
    # hsize = int((float(img.size[1]) * float(wpercent)))
    # printscreen_pil = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)
    #
    printscreen_pil= ImageGrab.grab()

    printscreen_numpy = np.array(printscreen_pil.getdata(), dtype='uint8') \
        .reshape((printscreen_pil.size[1], printscreen_pil.size[0], 3))

    # for video only
    # ret, frame = cap.read()
    # image = frame[0:500, 0:500]

    # for image only
    image = printscreen_numpy.copy()
    # gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # loop over the images to find the template in
    # for imagePath in glob.glob(args["images"] + "/*.jpg"):

    # load the image, convert it to grayscale, and initialize the
    # bookkeeping variable to keep track of the matched region
    # image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    found = None
    global_scale = 1
    global_maxCorr = 0;
    # loop over the scales of the image
    for scale in np.linspace(0.2, 1.0, 20)[::-1]:
        # resize the image according to the scale, and keep track
        # of the ratio of the resizing
        resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])

        # if the resized image is smaller than the template, then break
        # from the loop
        if resized.shape[0] < tH or resized.shape[1] < tW:
            global_scale = scale
            break

        # detect edges in the resized, grayscale image and apply template
        # matching to find the template in the image
        edged = cv2.Canny(resized, 50, 200)
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        # check to see if the iteration should be visualized
        if args.get("visualize", False):
            # draw a bounding box around the detected region
            clone = np.dstack([edged, edged, edged])
            cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
                (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
            cv2.imshow("Visualize", clone)
            cv2.waitKey(0)

        # if we have found a new maximum correlation value, then ipdate
        # the bookkeeping variable
        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)
            global_maxCorr = maxVal

    # unpack the bookkeeping varaible and compute the (x, y) coordinates
    # of the bounding box based on the resized ratio
    (_, maxLoc, r) = found
    (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
    (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

    # draw a bounding box around the detected result and display the image
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)

    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (20,20)
    fontScale = 0.5
    fontColor = (0, 255, 0)
    lineType = 2
    cv2.putText(image, "Scale: " + str(global_scale) + r"\nCorr: "+str(global_maxCorr),
                bottomLeftCornerOfText,
                font,
                fontScale,
                fontColor,
                lineType)

    cv2.imshow("Image", image)

    # Ff the 'q' key is pressed, stop the loop
    k = cv2.waitKey(0) & 0xFF
    if k == ord("q"):
        break
