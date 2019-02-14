# 
# Created by towshif ali (tali) on 2/11/2019
#

from template import Templates
from botVision import botVision
from AppControl import Controller
import time
import pyautogui

template = Templates()
vision = botVision()
# view1 = vision.get_screen_cv(1)
# view2 = vision.get_screen_cv(2)


controller = Controller(vision, template)

# 0 - click, 1 - search/wait
recipe_flow = [
    # ('new-recipe', 0),
    # ('foup', 0),
    # ('load-foup', 0),
    # ('loading-foup-dialog',1),
    # ('slot', 0),
    # ('load-wafer', 0),
    # ('loading-wafer-dialog', 1),
    # ('close-button',0),
    ('wafer-button', 0 ),
    ('alignment-button', 0),
    ('selectsites', 0),
    # ('alignment-sites-dialog', 0),
    # ('yes', 0),
    ('BF', 0),
    ('ok', 0),
    ('move_up', 0),
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

# if controller.wait_ui("setup-button") :
#     print('Scaling factor setup complete')
#

# pos = 0
# waiter = False
# while True and pos < len(recipe_flow) :
#     (action , atype) = recipe_flow [pos]
#
#     if atype == 0: # button click
#         print (pos, action, atype)
#         if controller.click_button(action):
#             pos += 1
#             print ( "click", action, "success!" )
#         else :
#             print ("Failed Click action.")
#
#     else : # wait timer
#         print(pos, action, atype)
#         if controller.wait_ui(action):
#             print ("Sleeping ...")
#             time.sleep(0.5)
#         else :
#             print (action, "ended!")
#             waiter = False
#             pos +=1



# Serpentine OM navigation @ 500un @ 5x

x = 0
y = 0
motion = 0  # 0 right # 1 left
xstep = 5
ystep = 5
while y < ystep :
    if motion == 0 :
        print ( x, y, motion)
        controller.click_button("move_right")
        pyautogui.press('esc')
        pyautogui.move(100,100)
        x += 1
        if x >= xstep:
            motion = 1
            controller.click_button("move_down")
            pyautogui.press('esc')
            pyautogui.move(100, 100)
            y += 1
            x -= 1
            print(x, y, motion)

    elif motion == 1 :
        print ( x, y, motion)
        controller.click_button("move_left")
        pyautogui.press('esc')
        pyautogui.move(100, 100)
        x -=1
        if x <= 0 :
            motion = 0
            print(x, y, motion)
            y +=1
            x += 1
            controller.click_button("move_down")
            pyautogui.press('esc')
            pyautogui.move(100, 100)
            #
    # elif motion == 2 :
    #     controller.click_button("move-down")

    time.sleep(0.5)

