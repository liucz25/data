#!/usr/bin/env python3

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def find_outlier(data):
    outlier=[]
    npd=np.array(data)

    #Q1=np.percentile(npd,25)
    #Q3=np.percentile(npd,75)

    datas=np.sort(data)
    #Q1=datas[int(0.25*len(data))]
    #Q3=datas[int(0.75*len(data))]
    n=len(datas)
    q1=(n+1)/4
    q2=2*(n+1)/4
    q3=3*(n+1)/4
    
    if (n+1)%4 == 0:
        Q1=datas[int(q1-1)]
        Q2=datas[int(q2-1)]
        Q3=datas[int(q3-1)]
    elif (n+1)%4 ==1:
        Q1=datas[int(q1-1)]*0.75+data[int(q1)]*0.25
        Q2=datas[int(q2-1)]*0.5+data[int(q2)]*0.5
        Q3=datas[int(q3-1)]*0.25+data[int(q3)]*0.75
    elif (n+1)%4 ==2:
        Q1=datas[int(q1-1)]*0.5+data[int(q1)]*0.5
        Q2=datas[int(q2-1)]
        Q3=datas[int(q3-1)]*0.5+data[int(q1)]*0.5
    elif (n+1)%4 ==3:
        Q1=datas[int(q1-1)]*0.25+data[int(q1)]*0.75
        Q2=datas[int(q2-1)]*0.5+data[int(q2)]*0.5
        Q3=datas[int(q3-1)]*0.75+data[int(q3)]*0.25
    print("")
    IQR=Q3-Q1
    min_val=Q1-1.5*IQR
    max_val=Q3+1.5*IQR
    print(n,q1,q2,q3,Q1,Q2,Q3,min_val,max_val)
    for i in datas:
        if i < min_val or i > max_val:
            outlier.append(i)


    return outlier

if __name__=='__main__':
    data=[1,4,3,6,7,9,12,15,16,18,20,25]
    list1=find_outlier(data)
    print(list1)

    
    #pdd=pd.DataFrame(np.array(data))
    p=plt.boxplot(data)
    outlier=p['fliers'][0].get_ydata()

    print(outlier)

    #print(pdd.describe())
    #plt.show()
