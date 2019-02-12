# 
# Created by towshif ali (tali) on 2/11/2019
#

from template import Templates
from botVision import botVision
from AppControl import Controller

template = Templates()
vision = botVision()
view1 = vision.get_screen_cv(1)
view2 = vision.get_screen_cv(2)

controller = Controller(vision, template)

recipe_flow = [
    'new-recipe',
    'select'
]

controller.click_button("foup")
