#!/usr/bin/env python3
# _*_ codeing:utf-8-

import pandas as pd


def test_score(test_feature,test_target):

    data = pd.read_csv("credit_card_train.csv",header=0)


    #score=model.score(test_feature,test_target)
    score=9
    return score

if __name__=='__main__':
    data = pd.read_csv("credit_card_train.csv",header=0)
    x,y=1,1
    xx1=data.iloc[:,1:14]
    xx2=data.iloc[:,15:17]
    yy=data.iloc[:.:18]

    score = test_score(x,y)

print("hello.")
print(xx2)
