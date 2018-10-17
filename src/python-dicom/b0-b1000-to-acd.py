#!/usr/bin/env python3

import pydicom
import numpy as np
import math
import matplotlib.pyplot as plt 


plt.cm 

ds0=pydicom.read_file('b0.dcm')  
ds1=pydicom.read_file('b1000.dcm')

ad=pydicom.read_file('3.dcm')

b0=ds0.pixel_array
b1=ds1.pixel_array

add=ad.pixel_array

sbl=np.array(b0)
sbh=np.array(b1)
adf=np.array(add)

bl=0
bh=1000

adc=np.log(sbh/sbl)/(bh-bl)

adct=adc*1000

plt.imshow(adc,cmap='gray_r')
#plt.imshow(adf,cmap='gray_r')
plt.show()
