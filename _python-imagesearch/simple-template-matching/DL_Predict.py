# 
# Created by towshif ali (tali) on 2/13/2019
#

# later...
from keras.models import model_from_json
import imageio
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import glob
import os
import csv

class DLPredictor:
    """
    Define your own custom method to deal with screen shot raw data.
    Of course, you can inherit from the ScreenShot class and change
    or add new methods.
    """

    def __init__(self):

        # CONSTANTS
        self.IMG_SIZE = 300

        # FOR TESTING
        self.IMG_DIR = 'images/All/'
        self.TEST_DIR = 'images/test'
        self.PREDICT_DIR = 'images/test2'
        self.tick = 0

        # load json and create model
        json_file = open('model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self.loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        self.loaded_model.load_weights("model.h5")
        print("Loaded model from disk")


    # def load_predict_data():
    #     predict_data = []
    #     for img in os.listdir(PREDICT_DIR):
    #         label = label_img(img)
    #         path = os.path.join(PREDICT_DIR, img)
    #         if "DS_Store" not in path:
    #             img = Image.open(path)
    #             img = img.convert('L')
    #             img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
    #             predict_data.append([np.array(img), label])
    #     # shuffle(test_data)
    #     return predict_data


    def predict(self, img):
        # predict_data = load_predict_data()
        #plt.imshow(test_data[10][0], cmap = 'gist_gray')

        predict_data = []
        label = np.array([0, 0])
        img = img.convert('L')
        img = img.resize((self.IMG_SIZE, self.IMG_SIZE), Image.ANTIALIAS)
        predict_data.append([np.array(img), label])

        predictImages = np.array([i[0] for i in predict_data]).reshape(-1, self.IMG_SIZE, self.IMG_SIZE, 1)
        predictLabels = np.array([i[1] for i in predict_data])

        predictions = self.loaded_model.predict(predictImages)

        classes = ["Scribe", "NonScribe"]
        predicted_class = classes[np.argmax(predictions[0])]
        # print(classes[np.argmax(predictions[0])])

        # i = 0
        # plt.imshow(predict_data[i][0], cmap=plt.cm.binary)
        # plt.show()
        # print (predictions[i])

        return (predictions, predicted_class)

