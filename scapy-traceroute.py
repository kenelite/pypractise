#/usr/bin/env python
# -*- coding: utf-8 -*- 

from scapy.all import *  
  
  
ans,unans=sr(IP(dst="www.qq.com",ttl=(2,25),id=RandShort())/TCP(flags=0x2),timeout=50)  
for snd,rcv in ans:  
    print snd.ttl,rcv.src,isinstance(rcv.payload,TCP)
