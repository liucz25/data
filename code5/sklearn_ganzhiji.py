#!/usr/bin/env python3

from matplotlib import pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron

data=pd.read_csv("two_class_data.csv",header=0)

feature = data[['x','y']].values
target = data['class'].values

x_train,x_test,y_train,y_test = train_test_split(feature,target,test_size=0.3,random_state=50)

#print(type(x_train))
#print(y_train.shape)
#print(y_test.shape)
plt.scatter(x_train[:,0],x_train[:,1],alpha=0.3)
model=Perceptron()

model.fit(x_train,y_train)

result = model.predict(x_test)

#print(result.shape)
plt.scatter(x_train[:,0],x_train[:,1],alpha=0.3)

plt.scatter(x_test[:,0],x_test[:,1],marker=',',c=y_test)

for i,txt in enumerate(result):
    plt.annotate(txt,(x_test[:,0][i],x_test[:,1][i]))

print(model.score(x_test,y_test))
#print(model.score(x_test,result))

plt.show()
