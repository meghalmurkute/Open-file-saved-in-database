# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:13:24 2020

@author: murku
"""

import MySQLdb
fil_name= input("Enter file name: ")
fil = fil_name+".txt"
f = open(fil,"w")
f.write("Hello "+fil_name)
f.close()
mydb= MySQLdb.connect(host="localhost", user="root", password="", database="demo")
mycursor = mydb.cursor()
mycursor.execute('insert into demo values ("'+fil_name+'","'+fil+'")')
mydb.commit()
mydb.close()
print("Inserted successfully!!!!!!")