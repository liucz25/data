#!/usr/bin/env python3
import matplotlib.pyplot as plt

import cc as cc
print(cc.adc)


plt.plot(cc.adc*1000000,cc.adf,".")
plt.show()