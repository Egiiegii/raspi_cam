"""
one_shot.py
take one photo

"""

import picamera
from time import sleep
from fractions import Fraction
from datetime import datetime
import os.path


shut_sp = 400000
iso_val = 100

port = 55000                # Reserve a port for your service.


with picamera.PiCamera() as camera:
    # get save name depending on time
    time = datetime.today()
    directory = "images/" + str(time.year) + "_" + str(time.month) + "_" + str(time.day)
    savename = "images/" + str(time.year) + "_" + str(time.month) + "_" + str(time.day) + "/" \
            + str(time.hour) + "_" + str(time.minute) + "_" + str(time.second) + ".png"
    print(savename)
    if not os.path.exists(directory):
         os.makedirs(directory)

    camera.resolution = (640, 480)
    # Set a framerate of 1/6fps, then set shutter
    # speed to 6s and ISO to 800
    # --------------- Take Photo using raspi
    camera.framerate = Fraction(1, 6)
    camera.shutter_speed = shut_sp
    camera.exposure_mode = 'off'
    camera.iso = iso_val
    camera.capture(savename)
    print("captured real ")



