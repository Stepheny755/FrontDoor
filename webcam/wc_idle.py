
from io import BytesIO
import numpy as np
import picamera
import picamera.array
import time
import cv2

class Idle():

    def __init__(self,cam):
        self.stream = BytesIO()
        self.camera = cam

    def check_activity(self):
        pass

    def get_image_capture_jpg(self):
        cam.capture(self.stream,"jpeg")
        print(self.stream)
        data = np.fromstring(self.stream.getvalue(),dtype=np.uint8)
        image = cv2.imdecode(data,1)
        image = image[:,:,::-1]
        print(data.shape)
        print(image.shape)
        return image

    def get_image_capture_bgr(self):
        with picamera.array.PiRGBArray(self.camera) as stream:
            self.camera.capture(stream,"bgr")
            image = stream.array[:,:,::-1]
            print(image.shape)
            return image

    def get_difference(self,i1,i2):
        pass

if(__name__=="__main__"):
    with picamera.PiCamera() as cam:
        i = Idle(cam)
        i.get_image_capture_bgr()
