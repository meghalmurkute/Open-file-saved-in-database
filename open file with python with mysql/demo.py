# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import MySQLdb
n = 1
mydb= MySQLdb.connect(host="localhost", user="root", password="", database="demo")
mycursor = mydb.cursor()
mycursor.execute("select name from demo")
result = mycursor.fetchall()
print("Files: ")
for i in result:
    print(n, " ", i[0])
    n=n+1
n=input("Choose which file to open: ")
q='select url from demo where name="'+n+'"'
mycursor.execute(q)
res = mycursor.fetchone()
fil=res[0]
mydb.close()
f = open(fil,"r")
print(f.read())
f.close()