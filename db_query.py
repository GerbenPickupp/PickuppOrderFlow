import mysql.connector 

def db_connect():
    mydb = mysql.connector.connect(
        host="pickupp-uat-12-aurora.cluster-c4tut00agkr8.ap-southeast-1.rds.amazonaws.com",
        user="pickupp",
        password="QcgALyevFSKDRXaUw4MGhL4UptY3QmCJ",
        database="uat"
        )      
    return mydb

def create_at():
    mydb = db_connect()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM create_id")
    myresult = mycursor.fetchall()
    return myresult