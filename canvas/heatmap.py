#!/usr/bin/python

from Adafruit_AMG88xx import Adafruit_AMG88xx
from time import sleep
#from PIL import Image

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import time


# sensor init
sensor = Adafruit_AMG88xx()

# startup time(AMG88xx)
sleep(.1)

d1 = sensor.readPixels()
d2 = np.array(d1).reshape(8,8)
#d2_i = Image.fromarray(np.uint8(d2))
#d2_64 = np.asarray(d2_i.resize((64, 64)))


#fig = plt.imshow(d2_64, cmap="inferno")
fig = plt.imshow(d2, cmap="inferno", interpolation='bicubic')
plt.colorbar()
plt.savefig('/home/pi/Desktop/map.png')

