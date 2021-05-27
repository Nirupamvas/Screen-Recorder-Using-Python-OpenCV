import datetime

from PIL import ImageGrab
import numpy as np
import cv2
#which captures windows API, which is for screen resolution
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
#we are saving the file in same file every time so we need to make it dynamic
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
#for saving video to local computer we need to encode, compress for that
#we are using cv2 fourcc with 4 parameters, and to save i.e, videowriter(filename, encoded file, frame rate, set(size))
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

webcam = cv2.VideoCapture(1)
while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    #we need to convert into numpy
    img_np = np.array(img)
    #for converting into RGB from BGR
    img_final =  cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _, frame = webcam.read()
    #Frame heigth of webcam
    fr_height, fr_width, _ = frame.shape
    img_final[0:fr_height, 0: fr_width, :] = frame[0: fr_height, 0: fr_width, :]
    #to display
    cv2.imshow('Secrete Capture', img_final)
    #we are taking out the frame
    #cv2.imshow('Webcam', frame)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break