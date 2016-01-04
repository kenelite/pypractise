#/usr/bin/env python
# -*- coding: utf-8 -*- 

from subprocess import call
import sys
import datetime
from datetime import *
import time

source = "/tmp/abc/*"
target = "/tmp/bcd"
rsync = "rsync"  #/usr/bin/rsync
arguments = "-av"
exclude = ".xdiff/"
logfile = "/tmp/rsync.log"

cmd = "%s %s --exclude %s %s %s --delete -i --log-file=%s"  %(rsync, arguments, exclude,  source, target, logfile)


def writetime():
    f=file(logfile,"a+")
    timeofnow=datetime.now().strftime('%b-%d-%y %H:%M:%S')
    f.write(timeofnow+'\n')
    f.close()

def sync():
    ret = call(cmd, shell=True)
    if ret !=0:
	print "rsync failed"
	sys.exit(1)


if __name__ == '__main__':
    try:
	writetime()
	begintime=datetime.now()

	sync()

	writetime()
	endtime=datetime.now()#.strftime('%b-%d-%y %H:%M:%S')
	print "Total cost time is %s seconds" % ((endtime - begintime).seconds)

    finally:
	print "rsync successfully." 
