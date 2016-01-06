#/usr/bin/env python
# -*- coding: utf-8 -*- 

import sqlite3


conn = sqlite3.connect('inventory.db')
cursor = conn.execute("insert into inventory_operatingsystem(name, description) values ('Windows', '2008 R2');")
cursor.fetchall()

conn.commit()
cursor1 = conn.execute('select * from inventory_operatingsystem;')
i = cursor1.fetchall()

print "%s" % i
