#/usr/bin/env python
# -*- coding: utf-8 -*- 

from threading import Thread
import subprocess
from Queue import * # Queue

num_threads = 3
queue = Queue()
ips = ["10.0.0.1", "10.0.0.51"]

def pinger(i, q):
    """ping subnet"""
    while True:
	ip = q.get()
	print "Thread %s: Pingping %s" % (i, ip)
	ret = subprocess.call("ping -c 1 %s" % ip,
				shell=True,
				stdout=open('/dev/null', 'w'),
				stderr=subprocess.STDOUT)
	if ret == 0:
	    print "%s: is alive" % ip
	else:
	    print "%s: did not respond" % ip


for i in range(num_threads):
    worker = Thread(target=pinger, args=(i, queue))
    worker.setDaemon(True)
    worker.start()
    for ip in ips:
	queue.put(ip)
	print "Main Thread Waiting"
	queue.join()
	print "Done"
