# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
import os
from tkinter import *
import time
# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def register_face(name):
	cap = cv2.VideoCapture(0)
	training=True;
	
	
	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()
	
		# Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
		# Detect faces in the image
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30)
			#flags = cv2.CV_HAAR_SCALE_IMAGE
		)
	
		print("Found {0} faces!".format(len(faces)))
		file_count=1;
		directory='dataset/faces/'+name
		print(directory)
		if training:
			if not os.path.exists(directory):
				os.makedirs(directory)
			else:
				path, dirs, files = next(os.walk(directory))
				file_count = len(files)+1
				
		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			
			face = gray[y:y+h, x:x+w]
			if training:
				faceResized=cv2.resize(face,(125, 150));
				cv2.imwrite(directory+'/a'+str(file_count)+'.png', faceResized);
				file_count=file_count+1
				del faceResized
			del face
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			"""//125 150
			Mat faceResized = new Mat();
			resize(face, faceResized, new Size(125, 150));
			String faceName = md.getAbsolutePath() + "/" + userid + "-" + name + "_" + System.currentTimeMillis() + ".png";
			imwrite(faceName, faceResized);
			"""
		# Display the resulting frame
		cv2.imshow('frame', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	
	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()





master = Tk()
e = Entry(master)
e.pack()

e.focus_set()

def callback():
	
	print(e.get()) # This is the text you may want to use later
	name=e.get()
	master.quit()
	register_face(name)
	
b = Button(master, text = "Start Face Registration", width = 10, command = callback)
b.pack()

mainloop()
