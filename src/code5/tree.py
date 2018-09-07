#!/usr/bin/env python3

from sklearn import datasets
from sklearn import tree
import numpy

#import graphviz

iris = datasets.load_iris()

#print(iris.data,iris.target)

x_train = iris.data[:120]
x_test = iris.data[120:]
y_train = iris.target[:120]
y_test = iris.target[120:]

model = tree.DecisionTreeClassifier(random_state=10)

#clf=model.fit(iris.data,iris.target)
model.fit(x_train,y_train)

print(model.score(x_test,y_test))

#dot_data = tree.export_graphviz(clf,out_file=None)
#graph = graphviz.Source(dot_data)

#graph.render("iris_dot")
