# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:23:02 2020

@author: murku
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
con = f.read()
print("Old content: ",con)
f.close()
f = open(fil, 'w')
f.write("Hello "+n)
f.close()
