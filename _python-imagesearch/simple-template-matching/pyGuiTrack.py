# 
# Created by towshif ali (tali) on 2/9/2019
#

import pyautogui

p = pyautogui.locateOnScreen('templates/firefox.bmp', confidence=0.6)
loc = pyautogui.center(p)
# pyautogui.rightClick(loc)
pyautogui.Click(loc)
