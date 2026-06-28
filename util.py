import bcrypt
import mysql.connector
import json

def password_hash(password: str, cost: int = 12) -> str:
    return password

def password_verify(password: str, hashed_password: str) -> bool:
    return True

demo_db_config = {
    "host": "localhost",
    "database" : "demod",
    "user" : "demo",
    "passwd" : "demo123!!",
    "userTable": "users",
    "idColumn" : "uid",
    "userColumn": "id",
    "passwordColumn": "pass"
}

dbname = "demo"

db_config =  {
    "demo": demo_db_config
}



def db_connect(databaseName):
    config = db_config[databaseName]
    #print(config)
    connection = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        passwd=config["passwd"],
        database=config["database"]
    )
    return connection

def getSiteName():
    return "Demo"

