from picamera import PiCamera
from io import BytesIO
import time

class Idle():

    def __init__(cam):
        self.stream = BytesIO()
        self.camera = cam

    def check_activity(self):
        cam.capture(self.stream,"jpeg")
        print(self.stream)
        data = np.fromstring(stream.getvalue(),dtype=np.uint8)
        print(data.shape)
        pass

    def get_difference(self,i1,i2):
        pass

if(__name__=="__main__"):
    i = Idle()
    i.check_activity()
