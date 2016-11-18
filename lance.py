#! /usr/bin/env python3


import shelve
import os

shelve_var=None
curr_db="No db opened yet"

# dont forget to perform chmod operations
import os.path

def getdb():
    return curr_db

def open(file_name):
    exist_flag=os.path.exists(file_name+".db")
    if not exist_flag:
        choice=str(input("The entered database doesn't exist would you like to  create one?"))
        if choice=="Y" or choice=="y":
            create(file_name)
        else:
            return
    else:
        global shelve_var
        global curr_db
        curr_db=file_name
        shelve_var=shelve.open(file_name,writeback=True)
        print("Database '"+file_name+"' Loaded into cache ...")

def create(file_name):
    global shelve_var
    if not os.path.exists(file_name+".db"):
        shelf_var=shelve.open(file_name,writeback=True)
        shelve_var=None
    else:
        print("Please enter a different database name as that database already exists!\n")
        create(str(input("Enter New Database name: ")))
    return

def insert(key,value):
    global shelve_var
    
    if shelve_var != None and  key not in shelve_var:
        shelve_var[key]=value
    else:
        print("Key already exists!")
    return

def find(key=None,value=None):
     global shelve_var
    # Should not be able to find key from value.... voilates the principle of Key based DBMS
    #   if key == None:
    #      for i in list(shelve_var):
    #         if shelve_var[i] is value:
    #              print(i)
     if value==None and key==None:
         dictx=dict()
         for x in shelve_var:
             dictx[x]=shelve_var[x]
         return dictx
     elif value == None:
         if key in shelve_var:
            return (shelve_var[key])
         else :
             print("Key doesnt exist in the database")
             
def update(key,value):
    global shelve_var
    print("(Key:Value) ("+str(key)+":"+str(shelve_var[key])+")===>(Key:New Value) ("+str(key)+":"+str(value)+") ")
    shelve_var[key]=value
    return

def delete(key):
    global shelve_var
    if key in shelve_var:
        print("The (Key:Value)===> ("+str(key)+":"+str(shelve_var[key])+") was deleted")
        del shelve_var[key]
    else:
        print("The key does not exist in the database.")

def removedb(file_name):
    global curr_db
    if file_name==curr_db:
        curr_db="No db opened yet"
    path = os.path.dirname(os.path.realpath(__file__))
    os.remove(path+"/"+file_name+".db")

def close():
    global curr_db
    global shelve_var

    if curr_db=="No db opened yet":
        print("No Db is open")
    else:
        print("Db '"+curr_db+"' has been closed")
        curr_db="No db opened yet"
        shelve_var=None