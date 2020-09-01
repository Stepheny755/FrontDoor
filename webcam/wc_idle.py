
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

        self.use_jpg = False
        self.activity_threshold = 0

        self.prev_image = get_image_capture()

    def check_activity(self):
        image = get_image_capture()
        print(get_difference(image,self.prev_image))

        pass

    def get_image_capture(self):
        if(self.use_jpg):
            return get_image_capture_jpg()
        else:
            return get_image_capture_bgr()

    def get_image_capture_jpg(self):
        cam.capture(self.stream,"jpeg")
        print(self.stream)
        data = np.fromstring(self.stream.getvalue(),dtype=np.uint8)
        image = cv2.imdecode(data,1)
        return self.bgr_to_rgb(image)

    def get_image_capture_bgr(self):
        with picamera.array.PiRGBArray(self.camera) as stream:
            self.camera.capture(stream,"bgr")
            image = stream.array
            return self.bgr_to_rgb(image)

    def bgr_to_rgb(self,image):
        return image[:,:,::-1]

    def get_difference(self,im1,im2):
        return xcorr_fft

    def xcorr_fft(self,x):
        return x.shape
        #x = np.fft2(np.pad(x,([0,0],[0,])))


if(__name__=="__main__"):
    with picamera.PiCamera() as cam:
        i = Idle(cam)
        i.get_image_capture_bgr()
