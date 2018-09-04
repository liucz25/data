#!/usr/bin/env python3

import json
import pandas as pd

def analysis(file,user_id):
    times = 0
    minutes = 0
    #return 

    f=open(file,'r')
    fj=pd.read_json(f)

    times=(fj[fj['user_id']==user_id]['minutes']).count()
    minutes=sum(fj[fj['user_id']==user_id]['minutes'])

    return times,minutes

if __name__=='__main__':
    file='../user_study.json'
    t,m=analysis(file,5348)
    print(t,m)
