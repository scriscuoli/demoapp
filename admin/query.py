import util
import mysql.connector
import subprocess
        


def getUser(uid):
    
    result = {
        "id" : 1,
        "user": "admin",
        "pass": "password"
    }
    return result

def getUserList():
    
    nres = []
    newRow = {
        "id": 1,
        "user" : "admin",
        "pass" : "password",
    }
    nres.append(newRow)
    return nres

def updateName(uid,newName):
    print("updating")

def updatePassword(uid,newPassword):
    print("update")

def deleteUser(uid):
    print("delete")

def addUser(name,pwd):
    print("addUser")