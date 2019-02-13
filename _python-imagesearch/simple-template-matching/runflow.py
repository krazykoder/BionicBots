# 
# Created by towshif ali (tali) on 2/11/2019
#

from template import Templates
from botVision import botVision
from AppControl import Controller
import time

template = Templates()
vision = botVision()
# view1 = vision.get_screen_cv(1)
# view2 = vision.get_screen_cv(2)


controller = Controller(vision, template)

# 0 - click, 1 - search/wait
recipe_flow = [
    # ('new-recipe', 0),
    ('foup', 0),
    ('load-foup', 0),
    ('loading-foup-dialog',1),
    ('slot', 0),
    ('load-wafer', 0),
    ('loading-wafer-dialog', 1),
    ('close-button',0),
    ('wafer-button', 0 ),
    ('alignment-button', 0),
    ('selectsites', 0),
    ('alignment-sites-dialog', 0),
    ('yes', 0),
    ('BF', 0),
    ('ok', 0),
    ('move_up', 0),
    ('cancel', 0),
    ('cancel', 0 ),
    ('end', 0),
    # ('end', 1),
    # ('end', 0),
    ('foup', 0),
    ('unload-wafer', 0),
    ('close-button', 0),
    ('end', 0),
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

    else : # wait timer
        print(pos, action, atype)
        if controller.wait_ui(action):
            print ("Sleeping ...")
            time.sleep(0.5)
        else :
            print (action, "ended!")
            waiter = False
            pos +=1
