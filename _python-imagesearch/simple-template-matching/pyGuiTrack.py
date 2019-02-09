# 
# Created by towshif ali (tali) on 2/9/2019
#

import pyautogui

p = pyautogui.locateOnScreen('templates/winlogo.bmp')
loc = pyautogui.center(p)

pyautogui.click(loc)