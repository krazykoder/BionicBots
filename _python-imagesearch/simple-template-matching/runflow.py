# 
# Created by towshif ali (tali) on 2/11/2019
#

from template import Templates
from botVision import botVision
from AppControl import Controller
from DL_Predict import DLPredictor
import time
from PIL import Image
import cv2
import numpy as np
import pyautogui

template = Templates()
vision = botVision()
predictor = DLPredictor()
controller = Controller(vision, template)


# view1 = vision.get_screen_cv(1)
# view2 = vision.get_screen_cv(2)

# 0 - click, 1 - search/wait, 2 - confirm/ wait 3 - key, 4 - write
recipe_flow = [
    ('foup', 0),
    ('load-foup', 0),
    ('loading-foup-dialog',1),
    ('slot', 0),
    ('load-wafer', 0),
    ('loading-wafer-dialog', 1),
    ('close-button',0),
    ('new-recipe', 0),
    # ('new-inspection', 2),
    ('HACKATON-RECIPE', 4),
    ('tab', 3),
    ('HACK-DEVICE', 4),
    ('tab', 3),
    ('HACK-LAYER', 4),
    ('tab', 3),
    ('new-inspection', 2)
    # ('ok', 0),
    # ('wafer-button', 0 ),
    # ('alignment-button', 0),
    # ('selectsites', 0),
    # ('alignment-sites-dialog', 0),
    # ('yes', 0),
    # ('BF', 0),
    # ('ok', 0),
    # ('move_up', 0),
    # ('cancel', 0),
    # ('cancel', 0 ),
    # ('end', 0),
    # # ('end', 1),
    # # ('end', 0),
    # ('foup', 0),
    # ('unload-wafer', 0),
    # ('close-button', 0),
    # ('end', 0),
]

# controller.click_button("foup")
# controller.click_button("load-foup")
# controller.click_button("new-recipe")
# controller.click_button("unload-wafer")
# controller.click_button("wafer-button")

time.sleep(3)

# setup scaling factor

if controller.wait_ui("setup-button") :
    print('Scaling factor setup complete')


pos = 0
waiter = False
while True and pos < len(recipe_flow) :
    (action , atype) = recipe_flow [pos]

    if atype == 0: # button click
        print (pos, action, atype)
        if controller.click_button(action):
            pos += 1
            print ( "click", action, "success!" )
        else :
            print ("Failed Click action.")

    elif atype == 1 : # wait timer
        print(pos, action, atype)
        if controller.wait_ui(action):
            print ("Sleeping ...")
            time.sleep(0.5)
        else :
            print (action, "ended!")
            waiter = False
            pos +=1

    elif atype == 2:
        print ("Wait UI atype 2 (confirm")
        while not controller.confirm_ui(action):
            time.sleep(0.25)

    elif atype == 3:
        print ("wait")
        pyautogui.press(action)
        pyautogui.move(100, 100)

    elif atype == 4:
        print ("Writing")
        pyautogui.typewrite(action, interval=0)  # useful for entering text, newline is Enter

# # Serpentine OM navigation @ 500un @ 5x
#
# x = 0
# y = 0
# motion = 0  # 0 right # 1 left
# xstep = 60
# ystep = 60
# while y < ystep :
#     if motion == 0 :
#         print ( x, y, motion)
#         controller.click_button("move_right")
#         pyautogui.press('esc')
#         pyautogui.move(100,100)
#         x += 1
#         if x >= xstep:
#             motion = 1
#             controller.click_button("move_down")
#             pyautogui.press('esc')
#             pyautogui.move(100, 100)
#             y += 1
#             x -= 1
#             print(x, y, motion)
#
#     elif motion == 1 :
#         print ( x, y, motion)
#         controller.click_button("move_left")
#         pyautogui.press('esc')
#         pyautogui.move(100, 100)
#         x -=1
#         if x <= 0 :
#             motion = 0
#             print(x, y, motion)
#             y +=1
#             x += 1
#             controller.click_button("move_down")
#             pyautogui.press('esc')
#             pyautogui.move(100, 100)
#             #
#     # elif motion == 2 :
#     #     controller.click_button("move-down")
#
#     time.sleep(0.25)

#
# # Predictor logic
# # set viewport
# # monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}
# # 1680x 1050
# monitor = {'top': 225, 'left': 540, 'width': 600, 'height': 600}
#
#
# while True:
#     viewPort = vision.get_screen_cv_port(2, monitor)
#     open_cv_image = np.array(viewPort)
#     # Convert RGB to BGR
#     open_cv_image = open_cv_image[:, :, ::-1].copy()
#
#     (result, classes) = predictor.predict(viewPort)
#
#
#     font = cv2.FONT_HERSHEY_DUPLEX  # color
#     # cv2.putText(frame, peop_conf , (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
#     cv2.putText(open_cv_image, classes + str(result[0]) , (0, 15), font, 0.5, (255, 255, 255), 1)
#
#     cv2.imshow('botView', open_cv_image)
#     k = cv2.waitKey(1)
#     if k == 27:  # Esc key to stop
#         break
#
#     # time.sleep(1)
#
