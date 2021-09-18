import cv2

vc = cv2.VideoCapture(0)

while True:
	success, img = vc.read()
	cv2.imshow("Video",img)
	if cv2.waitKey(30) & 0xFF==ord("q"):
		break

class Camera():

	def __init__(self,def_ref_rate:int=5,def_timeout:int=30):
		# internal parameters
		self.ref_rate = def_ref_rate
		self.timeout = def_timeout

		# capture content from video camera
		self.vc = cv2.VideoCapture(0)

	def __del__(self):
		self.vc.release()


	def show_image(self):
		success, img = self.vc.read()
		cv2.imshow("Capture",img)
