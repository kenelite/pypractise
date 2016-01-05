#/usr/bin/env python
# -*- coding: utf-8 -*- 

import subprocess
import time

IP_LIST = [ 'www.baidu.com',
'www.qq.com',
'www.taobao.com',
'www.xiaomi.com',
'www.jd.com',
'www.iqiyi.com']

cmd_stub = 'ping -c 5 %s'

def do_ping(addr):
    print time.asctime(), "DOING PING FOR", addr
    cmd = cmd_stub % (addr,)
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)


