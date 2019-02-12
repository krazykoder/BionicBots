import mss
from PIL import Image
import cv2
import numpy as np

class botVision:
    """
    Define your own custom method to deal with screen shot raw data.
    Of course, you can inherit from the ScreenShot class and change
    or add new methods.
    """

    def __init__(self):
    #     self.data = data
        self.monitor = 0

    def save_screen(self, screen, filename):
        with mss.mss() as sct:
            # filename = sct.shot(mon=screen, output='screen' + str(screen).replace('-1', '-All') + '.png')
            sct.shot(mon=screen, output=filename+'.png')

    def get_screen_PIL(self, screen):
        with mss.mss() as sct:
            #FOR PIL IMAGE
            img = sct.grab(sct.monitors[screen])
            image = Image.frombytes('RGB', img.size, img.rgb)
        return image

    def get_screen_cv (self, screen):
        with mss.mss() as sct:
            img = sct.grab(sct.monitors[0])
            img = Image.frombytes('RGB', img.size, img.rgb)
            # img.save("test.png")
            image = np.array(img)
            image = image[:, :, ::-1]  # rgb to brg for CV2 needed to reproduce original
        return image

    def view_cv (self):
        return


# ## Trial run
# with mss.mss() as sct:

#     # for screen in range(-1,4):
#     #     filename = sct.shot(mon=screen, output='screen'+str(screen).replace('-1','-All')+'.png')
#     #     # mon = -1 # for all screens together
#     #     print(filename)
#
#
#     # FOR PIL IMAGE
#     # img = sct.grab(sct.monitors[screen])
#     # image = Image.frombytes('RGB', img.size, img.rgb)
#     # image.save("testimage.png")
#
#     # FOR CV2
#     img = sct.grab(sct.monitors[0])
#     img = Image.frombytes('RGB', img.size, img.rgb)
#     # img.save("test.png")
#     image = np.array(img)
#     image = image[:, :, ::-1]  # rgb to brg for CV2 needed to reproduce original
#     cv2.imshow("Visualize", image)
#
#     cv2.waitKey(0)
#
