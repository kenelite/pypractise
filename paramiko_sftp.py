#/usr/bin/env python
# -*- coding: utf-8 -*- 


import paramiko
import os


hostname = '10.100.33.253'
port = 22
username = 'root'
password = '234567'
dir_path = '/home/admin/logs'
pkey_file = '/home/admin/.ssh/id_rsa'

if __name__ == "__main__":
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, pkey=key)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
	print 'Retrieving', f
	sftp.get(os.path.join(dir_path, f), f)
    t.close()
