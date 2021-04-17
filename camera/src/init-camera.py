import evdev
import picamera
from subprocess import check_output
from evdev import InputDevice, categorize, ecodes
import sys
import os
import random
import datetime
import time
import logging
from PIL import Image,ImageDraw,ImageFont
import traceback
picturesDir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pics')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
from waveshare_epd import epd2in13_V2


#bluetooth button
devices =[InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    if str(device.name) == 'Selfie Stick AU-Z06 Consumer Control':
        selfieStick = device

selfieStickBtn = 115
    
def printImage(img):
    logging.info("Printing to ePaper Display")
    epd = epd2in13_V2.EPD()
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    image = Image.open(os.path.join(picturesDir, img))
    epd.display(epd.getbuffer(image))
    time.sleep(2)

def snap():
    date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    img = date+'.jpg'
    logging.info("Capturing the image :",img)
    camera = picamera.PiCamera()
    camera.resolution =(122,250)
    camera.image_effect='film'
    camera.sharpness=(95)
    camera.color_effects =(128,128)
    camera.start_preview()
    time.sleep(8)
    camera.stop_preview()
    camera.capture(os.path.join(picturesDir, img))
    camera.close()
    printImage(img)
    
logging.basicConfig(level=logging.DEBUG)
try:
    logging.info("Starting Camera")
    #loop and wait for click event on selfie stick
    for event in selfieStick.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == 1:
                if event.code == selfieStickBtn:
                   snap()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()