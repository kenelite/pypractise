#/usr/bin/env python
# -*- coding: utf-8 -*- 


import paramiko

hostname = '10.100.33.253'
port = 2222
username = 'root'
password = '234567'

if __name__ == "__main__":
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    print stdout.read()
    s.close()
