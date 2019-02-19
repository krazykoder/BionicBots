# 
# Created by towshif ali (tali) on 2/11/2019
#

import mss
from PIL import Image
import cv2
import numpy as np


class Templates:

    def __init__(self):
        self.static_templates = {
            'new-recipe': 'assets/' + 'newrecipe' + '.bmp',
            'new-inspection': 'assets/' + 'new-inspection' + '.bmp',
            'setup-button': 'assets/' + 'setup' + '.bmp',
            'select-inspection': 'assets/' + 'selectinspection' + '.bmp',
            'wafer-button': 'assets/' + 'wafer' + '.bmp',
            'open-recipe-dialog': 'assets/' + 'openrecipedialog' + '.bmp',
            'loading-foup-dialog': 'assets/' + 'loading-foup-dialog' + '.bmp',
            'loading-wafer-dialog': 'assets/' + 'loading-wafer-dialog' + '.bmp',
            'load-foup': 'assets/' + 'load-foup' + '.bmp',
            'unload-foup': 'assets/' + 'unload-foup' + '.bmp',
            'foup': 'assets/' + 'foup' + '.bmp',
            'load-wafer': 'assets/' + 'load-wafer' + '.bmp',
            'unload-wafer': 'assets/' + 'unload-wafer' + '.bmp',
            'slot': 'assets/' + 'slot' + '.bmp',
            'loaded-slot': 'assets/' + 'loaded-slot' + '.bmp',
            'close-button': 'assets/' + 'close' + '.bmp',
            'ok': 'assets/' + 'ok' + '.bmp',
            'end': 'assets/' + 'end' + '.bmp',
            'alignment-button': 'assets/' + 'alignmentUIbutton' + '.bmp',
            'cancel': 'assets/' + 'cancel' + '.bmp',
            'next': 'assets/' + 'next' + '.bmp',
            'mark-site': 'assets/' + 'mark-site' + '.bmp',
            'selectsites': 'assets/' + 'selectsites' + '.bmp',
            'alignment-sites-dialog': 'assets/' + 'alignment-sites-dialog' + '.bmp',
            'yes': 'assets/' + 'yes' + '.bmp',
            'no': 'assets/' + 'no' + '.bmp',
            'alignment-sites-reselect': 'assets/' + 'alignment-sites-reselect' + '.bmp',
            'alignmentBFDFdialog': 'assets/' + 'alignmentBFDFdialog' + '.bmp',
            'DF': 'assets/' + 'DF' + '.bmp',
            'BF': 'assets/' + 'BF' + '.bmp',
            'alignmentdialogBF': 'assets/' + 'alignmentdialogBF' + '.bmp',
            'locatingwafercenterdialog': 'assets/' + 'locatingwafercenterdialog' + '.bmp',
            'movestagedialog': 'assets/' + 'movestagedialog' + '.bmp',
            'move_leftup': 'assets/' + 'move_leftup' + '.bmp',
            'move_up': 'assets/' + 'move_up' + '.bmp',
            'move_down': 'assets/' + 'move_down' + '.bmp',
            'move_left': 'assets/' + 'move_left' + '.bmp',
            'move_right': 'assets/' + 'move_right' + '.bmp'
            # 'foup': 'assets/' + 'foup' + '.bmp'
        }

        self.cvtemplates = {k: cv2.imread(v, 0) for (k, v) in self.static_templates.items()}
        self.templates = self.static_templates

