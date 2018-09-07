#!/usr/bin/env python3

from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data=pd.read_csv("three_class_data.csv",header=0)

feature = data[['x','y']].values
target = data['class'].values

x_train,x_test,y_train,y_test = train_test_split(feature,target,test_size=0.3,random_state=50)

model=KNeighborsClassifier()
model.fit(x_train,y_train)
results = model.predict(x_test)

print(model.score(x_test,y_test))

cm0=plt.cm.Oranges
cm1=plt.cm.Greens
cm2=plt.cm.Reds
cm_color = ListedColormap(['red','yellow'])
x_min, x_max = data['x'].min() -.5, data['x'].max()+.5
y_min, y_max = data['y'].min() -.5, data['y'].max()+.5

xx,yy=np.meshgrid(np.arange(x_min,x_max,.1), np.arange(y_min,y_max,.1))

z0 = model.predict_proba(np.c_[xx.ravel(),yy.ravel()])[:,0]
z1 = model.predict_proba(np.c_[xx.ravel(),yy.ravel()])[:,1]
z2 = model.predict_proba(np.c_[xx.ravel(),yy.ravel()])[:,2]

z0=z0.reshape(xx.shape)
z1=z1.reshape(xx.shape)
z2=z2.reshape(xx.shape)

plt.contourf(xx,yy,z0,camp=cm0,alpha=.9)
plt.contourf(xx,yy,z1,camp=cm1,alpha=.5)
plt.contourf(xx,yy,z2,camp=cm2,alpha=.4)

plt.scatter(x_train[:,0],x_train[:,1],c=y_train,cmap=cm_color)
plt.scatter(x_test[:,0],x_test[:,1],c=y_test,cmap=cm_color,edgecolors='black')
plt.show()
