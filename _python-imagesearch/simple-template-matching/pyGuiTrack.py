# 
# Created by towshif ali (tali) on 2/9/2019
#

import pyautogui
import PIL as Image

p = pyautogui.locateOnScreen('templates/chrome.bmp', confidence=0.8)
loc = pyautogui.center(p)
# pyautogui.rightClick(loc)
pyautogui.click(loc)
