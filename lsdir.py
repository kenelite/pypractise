#/usr/bin/env python
# -*- coding: utf-8 -*- 

import os,sys

path=sys.argv[1]

for dirpath,dirnames,filenames in os.walk(path):
    for file in filenames:
            fullpath=os.path.join(dirpath,file)
            print fullpath
