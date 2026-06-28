import util
import mysql.connector

dbname = util.dbname

def updatePassword(uid,newPassword):
    config = util.db_config[dbname]
    connection = util.db_connect(dbname)
    table=config["userTable"]
    icol=config["idColumn"]
    ucol=config["userColumn"]
    pcol=config["passwordColumn"]
    cursor = connection.cursor(dictionary=True)
    sqlString = f"update {table} set {pcol} = '{newPassword}' where  {icol} = {uid}"
    print(dbname + ": " + sqlString)
    cursor.execute(sqlString)
    connection.commit()

def getUser(uid):
    newRow = {
            "id": 1,
            "user" : "admin",
            "pass" : "password",
        }
    return newRow