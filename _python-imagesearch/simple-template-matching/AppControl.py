# 
# Created by towshif ali (tali) on 2/11/2019
#
import pyautogui
from botVision import botVision as sct
from template import Templates

# from pywinauto.application import Application
# app = Application().connect(process=7048)
# app = Application.Start(r'%windir%\system32\notepad.exe')

## Trial
# sct.save_screen(0,"hello")

import mss
from PIL import Image
import cv2
import numpy as np

class Controller:
    def __init__(self, vision, templates):
        self.vision = vision
        self.template = templates
        self.ratio = 1.0
        self.update = True
        # self.controller = controller
        # self.state = 'not started'


    def control(self):
        # self.template = Templates()
        return

    def click_button (self, button):
        print (self.template.templates[button])
        loc = self.locatebutton(button)

        if loc == (-1,-1):
            return False;
        else:
            pyautogui.click(loc)
            return True

    def wait_ui (self, button):
        print (self.template.templates[button])
        loc = self.locatebutton(button)

        if loc == (-1,-1):
            return False;
        else:
            # pyautogui.click(loc)
            return True

    def locatebutton(self, button):
        image = Image.open(self.template.templates[button])
        (tH, tW) = self.template.cvtemplates[button].shape[:2]
        try:
            if self.ratio != 1.0 :
                w, h = image.size
                width, height = int(w * self.ratio), int(h * self.ratio)
                image = image.resize((width, height), Image.ANTIALIAS)

            p = pyautogui.locateOnScreen(image, confidence=0.8)
            loc = pyautogui.center(p)
            # pyautogui.rightClick(loc)

            print("pyautogui clicked")

            return loc

        except :
            print("locate button failed... probably imput scaling problem. Trying scaling algo")

            if self.ratio == 1.0 :
                found = self.vision.find_scaled_image(self.vision.get_screen_cv(1), self.template.cvtemplates[button])
                (maxCorr, maxLoc, r, scale) = found
                self.ratio = r

            else :
                found = self.vision.find_in_image(self.vision.get_screen_cv(1), self.template.cvtemplates[button], 1/self.ratio)
                (maxCorr, maxLoc, r, scale) = found
            print(found)

            # # unpack the bookkeeping varaible and compute the (x, y) coordinates
            # # of the bounding box based on the resized ratio


            if maxCorr > 0.93:
                (startX, startY) = (int(maxLoc[0] * self.ratio), int(maxLoc[1] * self.ratio))
                (endX, endY) = (int((maxLoc[0] + tW) * self.ratio), int((maxLoc[1] + tH) * self.ratio))
                loc = ((startX + endX) / 2, (startY + endY) / 2)
            else :
                loc = (-1,-1)
                print ("Failed all image searches")
            pass

        return loc



