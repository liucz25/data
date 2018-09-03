#!/usr/bin/env python3
import json
import sys
filename="user_study.json"
with open(filename,'r')as f:
    datas=json.load(f)
    for data in datas:
        print(data["course"])
