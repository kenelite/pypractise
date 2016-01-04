#/usr/bin/env python
# -*- coding: utf-8 -*- 

import tarfile
import os

# make tar file
tar = tarfile.open("temp.tar", "w")
for root, dir, files in os.walk("/tmp/test"):
    for file in files:
	fullpath = os.path.join(root, file)
	tar.add(fullpath)
tar.close()


# make bzip2 file
bzip2 = tarfile.open("temp.tar.bzip2", "w|bz2")
for root, dir, files in os.walk("/tmp/test"):
    for file in files:
        fullpath = os.path.join(root, file)
        bzip2.add(fullpath)
bzip2.close()

# make gipz file
gzip = tarfile.open("temp.tar.gzip", "w|gz")
for root, dir, files in os.walk("/tmp/test"):
    for file in files:
        fullpath = os.path.join(root, file)
        gzip.add(fullpath)
gzip.close()

# list files of tar file
xtar = tarfile.open("temp.tar.gzip", "r|gz")
xtar.list()
xtar.name
xtar.getnames()
xtar.members
#xtar.extractall()
xtar.close()
