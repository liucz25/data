#!/usr/bin/env python3
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv("test_file.csv", header=0)

Total_Population = data["Total Population"]

p=plt.boxplot(Total_Population)
outlier=p['fliers'][0].get_ydata()

print(outlier)
plt.show()
