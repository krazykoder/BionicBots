import mss
from PIL import Image
import cv2
import numpy as np
import imutils


class botVision:
    """
    Define your own custom method to deal with screen shot raw data.
    Of course, you can inherit from the ScreenShot class and change
    or add new methods.
    """

    def __init__(self):
    #     self.data = data
        self.monitor = 0
        self.debug = False

    def save_screen(self, screen, filename):
        with mss.mss() as sct:
            # filename = sct.shot(mon=screen, output='screen' + str(screen).replace('-1', '-All') + '.png')
            sct.shot(mon=screen, output=filename+'.png')

    def get_screen_PIL(self, screen):
        with mss.mss() as sct:
            #FOR PIL IMAGE
            img = sct.grab(sct.monitors[screen])
            image = Image.frombytes('RGB', img.size, img.rgb)
        return image

    def get_screen_cv (self, screen):
        with mss.mss() as sct:
            img = sct.grab(sct.monitors[screen])
            img = Image.frombytes('RGB', img.size, img.rgb)
            # img.save("test.png")
            image = np.array(img)
            image = image[:, :, ::-1]  # rgb to brg for CV2 needed to reproduce original
        return image

    def view_cv (self):
        return


# ## Trial run
# with mss.mss() as sct:

#     # for screen in range(-1,4):
#     #     filename = sct.shot(mon=screen, output='screen'+str(screen).replace('-1','-All')+'.png')
#     #     # mon = -1 # for all screens together
#     #     print(filename)
#
#
#     # FOR PIL IMAGE
#     # img = sct.grab(sct.monitors[screen])
#     # image = Image.frombytes('RGB', img.size, img.rgb)
#     # image.save("testimage.png")
#
#     # FOR CV2
#     img = sct.grab(sct.monitors[0])
#     img = Image.frombytes('RGB', img.size, img.rgb)
#     # img.save("test.png")
#     image = np.array(img)
#     image = image[:, :, ::-1]  # rgb to brg for CV2 needed to reproduce original
#     cv2.imshow("Visualize", image)
#
#     cv2.waitKey(0)
#

    def find_scaled_image(self, image, template):

        (tH, tW) = template.shape[:2]

        # load the image, convert it to grayscale, and initialize the
        # bookkeeping variable to keep track of the matched region
        # image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        found = None

        # loop over the scales of the image
        for scale in np.linspace(0.5, 1.5, 20)[::-1]:
            # resize the image according to the scale, and keep track
            # of the ratio of the resizing
            resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
            r = gray.shape[1] / float(resized.shape[1])

            # if the resized image is smaller than the template, then break
            # from the loop
            if resized.shape[0] < tH or resized.shape[1] < tW:
                break

            # detect edges in the resized, grayscale image and apply template
            # matching to find the template in the image
            # edged = cv2.Canny(resized, 50, 200)
            edged = resized.copy()
            # blur = cv2.GaussianBlur(edged, (5, 5), 0)
            # ret3, edged = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF_NORMED)

            # TM_CCOEFF_NORMED for color images
            # TM_CCORR_NORMED for edged images ()
            # NORMED ~ [0,1] values

            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

            if self.debug :
                corr = result
                print("corr", maxVal, "ratio:", r, "scale", scale)
                # check to see if the iteration should be visualized

                # draw a bounding box around the detected region
                clone = np.dstack([edged, edged, edged])
                cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
                              (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
                cv2.imshow("Visualize", clone)
                cv2.waitKey(0)
            # time.sleep(1)

            # if we have found a new maximum correlation value, then ipdate
            # the bookkeeping variable
            if found is None or maxVal > found[0]:
                found = (maxVal, maxLoc, r, scale)
        return found

    def find_in_image(self, image, template, scale):


        (tH, tW) = template.shape[:2]

        # load the image, convert it to grayscale, and initialize the
        # bookkeeping variable to keep track of the matched region
        # image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        found = None

        # loop over the scales of the image
        # resize the image according to the scale, and keep track
        # of the ratio of the resizing
        resized = imutils.resize(gray, width=int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])

        # if the resized image is smaller than the template, then break
        # from the loop
        # if resized.shape[0] < tH or resized.shape[1] < tW:
        #     break

        # detect edges in the resized, grayscale image and apply template
        # matching to find the template in the image
        # edged = cv2.Canny(resized, 50, 200)
        edged = resized.copy()
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF_NORMED)

        # TM_CCOEFF_NORMED for color images
        # TM_CCORR_NORMED for edged images ()
        # NORMED ~ [0,1] values

        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        if self.debug:
            corr = result
            print("corr", maxVal, "ratio:", r, "scale", scale)
            # check to see if the iteration should be visualized

            # draw a bounding box around the detected region
            clone = np.dstack([edged, edged, edged])
            cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
                          (maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
            cv2.imshow("Visualize", clone)
            cv2.waitKey(0)
        # time.sleep(1)

        # if we have found a new maximum correlation value, then ipdate
        # the bookkeeping variable
        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r, scale)
        return found

    def getlocation(self, maxLoc, r, tW, tH):
        (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
        (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
        loc = ((startX + endX) / 2, (startY + endY) / 2)
        return loc
