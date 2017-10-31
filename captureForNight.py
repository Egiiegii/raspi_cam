import picamera
from time import sleep
from fractions import Fraction
from datetime import datetime
import os.path

shut_sp = 1225000
iso_val = 100
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    #while True:
        #print("waiting press the key")
        #k = cv2.waitKey(1) & 0xFF

        # set file name
    time = datetime.today()
    directory = "images/" + str(time.year) + "_" + str(time.month) + "_" + str(time.day)
    savename = "images/" + str(time.year) + "_" + str(time.month) + "_" + str(time.day) + "/" \
            + str(time.hour) + "_" + str(time.minute) + "_" + str(time.second) + ".png"
    print(savename)
    if not os.path.exists(directory):
         os.makedirs(directory)

    # set framerate of 1/6fps, then set shutter
    # speed to 6s and ISO to 450
    camera.framerate = Fraction(1, 6)
    camera.shutter_speed = shut_sp
    camera.exposure_mode = 'off'
    camera.iso = iso_val
    # Give the camera a good long time to measure AWB
    # (you may wish to use fixed AWB instead)
    sleep(10)
    # Finally, capture an image with a 6s exposure. Due
    # to mode switching on the still port, this will take
    # longer than 6 seconds
    time = '{0:%Y_%m_%d_%H_%M_%S}'.format(datetime.now())
    camera.capture("temp.png")
    print("captured black ")

    time = datetime.today()
    directory = "images/" + str(time.year) + "_" + str(time.month) + "_" + str(time.day)
    savename = "images/" + str(time.year) + "_" + str(time.month) + "_" + str(time.day) + "/" \
            + str(time.hour) + "_" + str(time.minute) + "_" + str(time.second) + ".png"
    print(savename)
    if not os.path.exists(directory):
         os.makedirs(directory)

    # set framerate of 1/6fps, then set shutter
    # speed to 6s and ISO to 450
    camera.framerate = Fraction(1, 6)
    camera.shutter_speed = shut_sp
    camera.exposure_mode = 'off'
    camera.iso = iso_val
    # Give the camera a good long time to measure AWB
    # (you may wish to use fixed AWB instead)
    sleep(10)
    # Finally, capture an image with a 6s exposure. Due
    # to mode switching on the still port, this will take
    # longer than 6 seconds
    time = '{0:%Y_%m_%d_%H_%M_%S}'.format(datetime.now())
    camera.capture(savename)
    print("captured real ")
