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

################################################################################################################
################################################################################################################
################################################################################################################



def Fund_Performance_Writer(cnx, cursor):
    #the mysql command being define here 
    sql_Command = "INSERT INTO Fund_Performance (Fund_Classification, Date_Time, total_account, amount_gain_lost) VALUES (%s, %s, %s, %s)"
    value = (1, datetime.today() , 0.0, -0.3)

    cursor.execute(sql_Command, value)

    
################################################################################################################
################################################################################################################
################################################################################################################

def All_Accounts_Writer(cnx, cursor):
    
    sql_Command = "INSERT INTO All_Accounts_Balance (total_accounts, Gain_Loss, Date_Time, opening_value ) VALUES (%s, %s, %s, %s)"
    value = (199.01, 00.45, datetime.today(), 1)

    cursor.execute(sql_Command, value)

    

################################################################################################################
################################################################################################################
################################################################################################################

def Own_Stock(cnx, cursor):
    
    sql_Command = """ INSERT INTO Own_Stock ( stock_name, fund_classification, stock_price_buying_time, amount_bought, today_gain, total_gain, percent_position_in_fund, Date_Time_Purchase )
                                    VALUES  (  %s, %s, %s, %s, %s, %s, %s, %s)"""


    value = ("Tesla", 2, 100.20, 0.005, +100.34, -1.45, 0.050, datetime.today())

    cursor.execute(sql_Command, value)

    


################################################################################################################
################################################################################################################
################################################################################################################

def Sold_Stock(cnx,cursor):
    sql_Command =  """ INSERT INTO Sold_Stock ( Fund_Classification, stock_name,  amount_sold_usd,  Date_Time)  VALUES ( %s, %s, %s, %s)"""


    value = (1, "Tesla", 0.34, datetime.today())

    cursor.execute(sql_Command,  value)

################################################################################################################
################################################################################################################
################################################################################################################



cnx, cursor = connection_establisher()

Fund_Performance_Writer(cnx, cursor)

All_Accounts_Writer(cnx, cursor)

Own_Stock(cnx, cursor)

Sold_Stock(cnx, cursor)

cnx.commit()
cnx.close()