import cv2

class Camera():

    def __init__(self, def_ref_rate: int = 5, def_timeout: int = 30):
        # internal parameters
        self.passive_ref_rate = def_ref_rate
        self.timeout = def_timeout

        # capture content from video camera
        self.vc = cv2.VideoCapture(0)

        self.detection_baseline = None

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
        if(self.detection_baseline==None):
            self.detection_baseline = frame
            return

        delta = cv2.absdiff(detection_baseline,frame)
        filtered = cv2.threshold(delta,50,255,cv2.THRESH_BINARY)

        cv2.findContours(filtered,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) < 5000:
                continue
            (x, y, w, h)=cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 1)

        cv2.imshow("Objects",frame)

        return

if(__name__=="__main__"):
    c = Camera()
    while True:
        c.detect_motion()
