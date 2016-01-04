#/usr/bin/env python
# -*- coding: utf-8 -*- 

import hashlib
def create_checksum(path):
    """
    Reads in file. Create chechsum of file line by line.
    Returns complete checksum total for file.
    """

    fp = open(path)
    checksum = hashlib.md5()
    while True:
	buffer = fp.read(8192)
	if not buffer:break
	checksum.update(buffer)
    fp.close()

    chechsum = checksum.digest()
    return checksum
