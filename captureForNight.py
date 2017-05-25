import picamera
from time import sleep
from fractions import Fraction
from datetime import datetime


shut_sp = 1250000
iso_val = 450
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    # Set a framerate of 1/6fps, then set shutter
    # speed to 6s and ISO to 800
    while True:
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
        camera.capture('Pictures/'+time+'.jpg')
        print("captured")
	sleep(60 * 30)
