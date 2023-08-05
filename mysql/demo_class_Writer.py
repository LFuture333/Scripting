import mysql.connector
from datetime import datetime, time

#Database Log-in Configuration file
config = {
    "host": "localhost",
    "port": "3306",
    "database": "Finance_ai",
    "user": "access_ai",
    "password": "T$4kgndsngsg(%",
    "use_unicode": True,
    "get_warnings": True,
}


#Connection extablish with the mysql server 

def connection_establisher():
    cnx = mysql.connector.Connect(**config)

    cursor = cnx.cursor()

    return cnx, cursor


def Fund_Performance_Writer(cnx, cursor):
    #the mysql command being define here 
    sql_Command = "INSERT INTO Fund_Performance (Fund_Classification, Date_Time, total_account, amount_gain_lost) VALUES (%s, %s, %s, %s)"
    value = (1, datetime.today() , 0.0, -0.3)

    cursor.execute(sql_Command, value)

    cnx.commit()




cnx, cursor = connection_establisher()

Fund_Performance_Writer(cnx, cursor)