import cv2
import sys
import os
import numpy as np
import pdb
import pickle

(CV_MAJOR_VER, CV_MINOR_VER, mv1) = cv2.__version__.split(".")
current_directory=os.path.dirname(os.path.abspath(__file__))
# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
current_directory='dataset/faces/'

RECOGNITION_ALGORITHM = 1
POSITIVE_THRESHOLD = 80

def is_cv3():
    if CV_MAJOR_VER == 3:
        return True
    else:
        return False

def model(algorithm, thresh):
    # set the choosen algorithm
    model = None
    if algorithm == 1:
        model = cv2.face.LBPHFaceRecognizer_create()
    elif algorithm == 2:
        model = cv2.face.FisherFaceRecognizer_create()
    elif algorithm == 3:
        model = cv2.face.EigenFaceRecognizer_create()
    else:
        print("WARNING: face algorithm must be in the range 1-3")
        os._exit(1)
    return model 

def get_images_and_labels():
    global current_directory
    image_paths=[]
    images=[]
    labels=[]
    label=0
    if(os.path.isdir(current_directory)==True):
        b = os.listdir(current_directory)
        for face_names in b:
            path=current_directory+'\\'+face_names
            label=label+1
            for filename in os.listdir(path):
                image_path=path+'\\'+filename
                img = cv2.imread(image_path,0)
                # Convert the image format into numpy array
                image = np.array(img, 'uint8')
                # Get the label of the image
                # If face is detected, append the face to images and the label to labels
                images.append(image)
                labels.append(label)

    return images, labels

model = cv2.face.LBPHFaceRecognizer_create()
images, labels = get_images_and_labels()
model.train(images, np.array(labels))
#help(model)
model.write('recognizer.yml')


