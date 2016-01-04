#/usr/bin/env python
# -*- coding: utf-8 -*- 

import platform

"""
Finggerprints the following Operating Systems:

* Mac OS X
* Ubuntu
* Red Hat / Cent OS
* FreeBSD
* SunOS
"""

class OpSysType(object):
    """Determins OS Type using platfor module"""
    def __getattr__(self, attr):
	if attr == "osx":
	    return "Mac OS X"
	elif attr == "rhel":
	    return "Redhat"
	elif attr == "ubu":
	    return "Ubuntu"
	elif attr == "fbsd":
	    return "FreeBSD"
	elif attr == "sun":
	    return "SunOS"
	elif attr == "unknown_linux":
	    return "unknown"
	else:
	    raise AttributeError, attr
    
    def linuxType(self):
   # """Uses various methods to determine linux type"""

	if platform.dist()[0] == self.rhel:
	    return self.rhel
	elif platform.uname()[1] == self.ubu:
	    return self.ubu
	else:
	    return self.unknown_linux

    def queryOS(self):
	if platform.system() == "Darwin":
	    return self.osx
	elif platform.system() == "Linux":
	    return self.linuxType()
	elif platform.system() == self.sun:
	    return self.sun
	elif platform.system() == self.fbsd:
	    return self.fbsd

def fingerprint():
    type = OpSysType()
    print type.queryOS()

if __name__ == "__main__":
    fingerprint()
