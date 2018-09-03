#!/usr/bin/env python3

import json


def ananlysis(file,user_id):
    time = 0
    minutes = 0


    return time,minutes

if __name__=='__main__':
    file = 'b.txt'
    fobj=open(file)
    ft=fobj.read()
    ftxt=ft[1:-4]
    txt=json.loads(ftxt)
    print(txt["user_id"])


