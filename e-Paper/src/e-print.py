import sys
import os
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import logging
assets = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'libs')
if os.path.exists(libdir):
    sys.path.append(libdir)
from waveshare_epd import epd2in13_V2
logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("Printing to ePaper Display")
    epd = epd2in13_V2.EPD()
    epd.init(epd.FULL_UPDATE)
    font38 = ImageFont.truetype(os.path.join(assets, 'Poppins-SemiBold.ttf'), 38)
    font24 = ImageFont.truetype(os.path.join(assets, 'Font.ttc'), 24)
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), 'David Balan', font = font38, fill = 0)
    draw.text((10, 45), 'Python ePaper Camera', font = font24, fill = 0)
    epd.display(epd.getbuffer(image))
    time.sleep(2)
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
