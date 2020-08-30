from picamera import PiCamera
from io import IOBytes
import time

class Idle():

    def __init__(cam):
        self.stream = IOBytes()
        self.camera = cam
