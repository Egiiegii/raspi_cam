import picamera
from time import sleep
from fractions import Fraction
from datetime import datetime
import os.path

shut_sp = 400000
iso_val = 100

with picamera.PiCamera() as camera:
    # get save name depending on time
    time = datetime.today()
    directory = "images/" + str(time.year) + "_" + str(time.month) + "_" + str(time.day)
    savename = "images/" + str(time.year) + "_" + str(time.month) + "_" + str(time.day) + "/" \
            + str(time.hour) + "_" + str(time.minute) + "_" + str(time.second) + ".png"
    print(savename)
    if not os.path.exists(directory):
         os.makedirs(directory)

    # take picture
    camera.resolution = (640, 480)
    camera.framerate = Fraction(1, 6)
    camera.shutter_speed = shut_sp
    camera.exposure_mode = 'off'
    camera.iso = iso_val
    time = '{0:%Y_%m_%d_%H_%M_%S}'.format(datetime.now())
    camera.capture(savename)
    print("captured real ")
