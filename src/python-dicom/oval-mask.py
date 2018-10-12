#!/usr/bin/env python3
import numpy as np
from PIL import Image
import matplotlib.pyplot as pyplot

data_b=np.arange(80000)
data=data_b.reshape(400,200)

w,h = data.shape
a=w/2
b=h/2
mask=np.zeros(data.shape)
i=0
while (i <w):
	j=0
	while (j<h):
		x=i-a+0.5
		y=j-b+0.5
		edge=((x**2)/(a**2))+((y**2)/(b**2))
		if (edge>=1.0):
			mask[i][j]=1
		#mask[i][j]=edge
		j+=1
	i+=1
pyplot.imshow(mask)
pyplot.show()

#np.savetxt("mask.txt",mask)

#below error,i think PIL fromarray loc err

#im=Image.fromarray(mask)
#im=im.convert("1")
#im.save("im.jpg")
#im.show()

#PIL im.save()must affter convert cannot use fromarray(im,"mode")
