# 
# Created by towshif ali (tali) on 2/11/2019
#
import pyautogui
from botVision import botVision as sct
from template import Templates
import multiscale_match

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
        # self.controller = controller
        # self.state = 'not started'
    def control(self):
        # self.template = Templates()
        return

    def click_button (self, button):
        print (self.template.templates[button])
        loc = self.locatebutton(button)
        pyautogui.click(loc)
        return

    def locatebutton(self, button):
        try:
            p = pyautogui.locateOnScreen(self.template.templates[button], confidence=0.8)
            loc = pyautogui.center(p)
            # pyautogui.rightClick(loc)
            return loc
        except:
            print("locate button failed... probably imput scaling problem. Trying scaling algo")
            



