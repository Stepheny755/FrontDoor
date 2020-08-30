from picamera import PiCamera
from io import IOBytes
import time

class Idle():

    def __init__(cam):
        self.stream = IOBytes()
        self.camera = cam

    def check_act(self):
        cam.capture(self.stream,"jpeg")
        print(self.stream)
        data = np.fromstring(stream.getvalue(),dtype=np.uint8)
        print(data.shape)
        pass

    def get_difference(self,i1,i2):
        pass
