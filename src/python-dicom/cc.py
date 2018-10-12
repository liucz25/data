#!/usr/bin/env python3

import pandas as pd
import numpy as np
import bb as bb

d=[]
adc=np.array(bb.adc[100:200,100:200].flat)
d.append(adc)
d.append(bb.adf[100:200,100:200])
adf=np.array(bb.adf[100:200,100:200].flat)
print("\n")

df=pd.DataFrame({"adc":adc,"adf":adf})



print(df.corr())
