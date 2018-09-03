#!/usr/bin/env python3

import json


def analysis(file,user_id):
    time = 0
    minutes = 0

    fobj=open(file)
    ft=fobj.read()
    ftxt=ft[0:-5]
    l=[]
    l=ftxt.split("}")
   
    for ls in l:
        txt=json.loads(ls[1::]+'}')
        #print(txt['course'])
        if txt['user_id']==user_id:
            time += 1
            minutes += txt['minutes']

    return time,minutes

if __name__=='__main__':
    file = 'user_study.json'
    user_id = 199071

    t,m=analysis(file,user_id)
    print(t,m)
   
