#/usr/bin/env python
# -*- coding: utf-8 -*- 


import smtplib
import subprocess
import string


p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
MSG = p.stdout.read()
FROM = "user@devcentos.example.com"
TO = "root@devcentos.example.com"
SUBJECT = "Nightly Disk Usage Report"
msg = string.join((
	"From: %s" % FROM,
	"TO: %s" % TO,
	"Subject: %s" % SUBJECT,
	"",
	MSG),"\r\n")


server = smtplib.SMTP('localhost')
server.sendmail(FROM, TO, msg)
server.quit()
