import os 
from coinbase.wallet.client import Client
import Extracting_Credentials as EC
import json

file_Path="/Users/louisfuture/Documents/coinbase_Key/Key.json"


Api_Key, Api_Secret = EC.Extract_Credentials(file_Path=file_Path)


#Connect Get client information

client= Client(Api_Key, Api_Secret)


def Get_accountID(client):

    data = client.get_primary_account()

    print(data)

    account_ID = data['id']
    print(account_ID)

def Accounts_json(client):
    data = client.get_primary_account()
    
    json_object = json.dumps(data, indent=4)

    with open("Accounts.json", 'w') as outfile:
        outfile.write(json_object)


Accounts_json(client)

Get_accountID(client)