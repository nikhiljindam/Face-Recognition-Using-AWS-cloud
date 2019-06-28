import cv2
import sys
import os
import numpy as np
import pdb
import pickle
import base64
import socket
import time
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer.yml')
# Get user supplied values
ADDRESS = ("13.***.96.***", 7813)
response = ("13.***.96.***", 7812)
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

cap = cv2.VideoCapture(0)
training = True
font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 500)
fontScale              = 1
fontColor              = (255,255,255)
lineType               = 2


while(True):
    # Capture frame-by-frame
    ret, image = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    print("Found {0} faces!".format(len(faces)))
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        faceResized=cv2.resize(face, (125, 150));
        cv2.imwrite("img.png",faceResized)
        with open("img.png", "rb") as imageFile:
            str = base64.b64encode(imageFile.read())
            print(len(str))
            s = socket.socket()
            print(ADDRESS)
            s.connect(ADDRESS)
            s.send(str)
            s.close()
            s = socket.socket()
            s.connect(response)
            s.send(str)
            reciver = s.recv(1024)
            print(reciver)
            s.close()
            bb = reciver.decode("utf-8") 
            nbr_predicted = bb.split('#')
            ans = nbr_predicted[0] 
            print(nbr_predicted[0])
            print(nbr_predicted[1])
            print('------------------------------')
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(image,ans,(x,y-10),font,fontScale,fontColor,lineType)
        
    cv2.imshow("Faces found", image)
    cv2.waitKey(1)
