import numpy as np
import cv2

class Camera():

    def __init__(self, def_ref_rate: int = 5, def_timeout: int = 30):
        # internal parameters
        self.passive_ref_rate = def_ref_rate
        self.timeout = def_timeout

        # camera resolution
        self.res_w = 640
        self.res_h = 480

        # capture content from video camera
        self.vc = cv2.VideoCapture(0)

        _, self.detection_baseline = self.vc.read()
        self.detection_baseline = cv2.cvtColor(self.detection_baseline,cv2.COLOR_BGR2GRAY)
        self.detection_baseline = cv2.GaussianBlur(self.detection_baseline,(25,25),0)

    def __del__(self):
        self.vc.release()

    def show_image(self):
        success, img = self.vc.read()
        cv2.imshow("Capture", img)

    def detect_motion(self):
        success, img = self.vc.read()
        frame = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        frame = cv2.GaussianBlur(frame,(25,25),0)

        # exit if camera recently initialized
        #if(self.detection_baseline==None):
        #    self.detection_baseline = frame
        #    return
        #print((frame.shape))
        #print((self.detection_baseline.shape))

        delta = cv2.absdiff(self.detection_baseline,frame)
        filtered = cv2.threshold(delta,50,255,cv2.THRESH_BINARY)[1]

        contours = cv2.findContours(filtered,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

        if(contours is not None):
            for contour in contours:
                if cv2.contourArea(contour) < 5000:
                    continue
                (x, y, w, h)=cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 1)

        self.detection_baseline = frame

        cv2.imshow("Objects",frame)

        return

    def get_baseline(self):
        return self.detection_baseline

if(__name__=="__main__"):
    c = Camera()
    while True:
        c.detect_motion()
        cv2.imshow("Baseline",c.get_baseline())
        key = cv2.waitKey(30)
        if(key==ord("q")):
            break
