#!/usr/bin/python

from Adafruit_AMG88xx import Adafruit_AMG88xx
from time import sleep

import numpy as np
import pandas as pd

sensor = Adafruit_AMG88xx()

sleep(.1)
d1 = sensor.readPixels()
d2 = np.array(d1).reshape(8,8)
print(d2)

df = pd.DataFrame(d2)
print(df)

