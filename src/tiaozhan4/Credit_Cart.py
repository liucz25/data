#!/usr/bin/env python3
# _*_ codeing:utf-8-

import pandas as pd


def test_score(test_feature,test_target):

    data = pd.read_csv("credit_card_train.csv",header=0)


    score=model.score(test_feature,test_target)

    return score

if __name__=='__main__':
    score = test_score(x,y)

print("hello.")
print(s)
