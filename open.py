import numpy as np
import cv2
import time, os

filename = "video_{0}.avi".format(int(time.time()))
fps = 18.0
resolution = '720p' # screen resolution


def change_resolution(cap, width, height):
    """
    :cap: the video capture instance
    :width: video width
    :height: video height
    """
    cap.set(3, width)
    cap.set(4, height)


def get_dims(cap, res="1080p"):
    """
    :cap: 
    """
    width, height = STD_DIMENSIONS['480p']
    if res in STD_DIMENSIONS:
         width, height = STD_DIMENSIONS[res]
    change_resolution(cap, width, height)
    return width, height

# Standard video dimension sizes
STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160)
}

VIDEO_TYPES = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID')
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPES:
        return VIDEO_TYPES[ext]
    return VIDEO_TYPES['avi']

cap = cv2.VideoCapture(0)

dims = get_dims(cap, res=resolution)
video_type_cv2 = get_video_type(filename)

out = cv2.VideoWriter(filename, video_type_cv2, fps, dims)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    

    # Our operations on the frame come here
    # if you want to change the frame color
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    # Display the resulting frame
    # cv2.imshow('frame',frame)
    # cv2.imshow('gray',gray)

    # if ord('p') and ret:
        # namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
        # imshow("cam-test",img)
        # waitKey(0)
        # destroyWindow("cam-test")
        # imwrite("filename_{}.jpg".format(int(time.time())),img) #save image
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()