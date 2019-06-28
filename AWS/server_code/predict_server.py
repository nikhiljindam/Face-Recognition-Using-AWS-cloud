import cv2
import socket
import sys
import os
import numpy as np
import pdb
import pickle
import base64
import _time
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer.yml')
HOST = ''	# Symbolic name, meaning all available interfaces
PORT = 7812	# Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
def readImage(incommingData):
    imageName = "imageToSave.png"
    fh = open(imageName, "wb")
    #ba = bytearray(base64.b64decode(message))
    fh.write(base64.b64decode(incommingData)) 
    #.decode('base64'))
    fh.close()
#Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()
	
print('Socket bind complete')

#Start listening on socket
s.listen(10)
print( 'Socket now listening')

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
	conn, addr = s.accept()
	print( 'Connected with ' + addr[0] + ':' + str(addr[1]))
	try:
		image = ""
		data = conn.recv(1024).decode()
		'''
		while True:
			data = conn.recv(1024).decode()
			print(len(image))
			if(not data):
				break
			image = image + data
		print(len(image))
		readImage(image)
		'''
		image_path="imageToSave.png"
		exists = os. path. isfile(image_path)
		if(exists):
			#filename =image_path
			print('recieved Data')

			gray = cv2.imread("imageToSave.png",0)
			# Our operations on the frame come here

			#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

			nbr_predicted, conf = recognizer.predict(gray)
			print(nbr_predicted)
			print(conf)
			r=str(nbr_predicted)+"#"+str(conf)
			print('------------------------------')            
			print(r)
			conn.send(r.encode())
	except:
		type, value, traceback = sys.exc_info()
		print('Error opening %s: %s' % (value.filename, value.strerror))
		conn.close()
s.close()
'''
#gray = cv2.imread('dataset/testing/a33.png',0)
# Our operations on the frame come here

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

nbr_predicted, conf = recognizer.predict(gray)

print(nbr_predicted)
print(conf)
print('------------------------------')
'''