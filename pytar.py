#/usr/bin/env python
# -*- coding: utf-8 -*- 

import tarfile
import os

tar = tarfile.open("temp.tar", "w")
for root, dir, files in os.walk("/tmp/test"):
    for file in files:
	fullpath = os.path.join(root, file)
	tar.add(fullpath)
tar.close()





bzip2 = tarfile.open("temp.tar.bzip2", "w|bz2")
for root, dir, files in os.walk("/tmp/test"):
    for file in files:
        fullpath = os.path.join(root, file)
        bzip2.add(fullpath)
bzip2.close()

gzip = tarfile.open("temp.tar.gzip", "w|gz")
for root, dir, files in os.walk("/tmp/test"):
    for file in files:
        fullpath = os.path.join(root, file)
        gzip.add(fullpath)
gzip.close()

xtar = tarfile.open("temp.tar.gzip", "r|gz")
xtar.list()
xtar.close()
