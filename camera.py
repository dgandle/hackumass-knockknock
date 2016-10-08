from picamera import PiCamera , Color
from time import sleep
import PIL
from PIL import Image


import time
ts = time.time()
import datetime
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

camera = PiCamera()

camera.start_preview()

camera.annotate_text = st
camera.annotate_text_size = 50
camera.annotate_background = Color(0,0,0)
camera.annotate_background = Color('black')
sleep(2)

camera.capture('/home/pi/Web Server/static/image.jpg')
    
camera.stop_preview()

