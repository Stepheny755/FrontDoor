from picamera import PiCamera
from io import IOBytes
import time



if(__name__=="__main__"):
    stream = IOBytes()
    with PiCamera() as cam:
        cam.capture(stream,"jpeg")
