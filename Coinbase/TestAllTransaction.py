import os 
from coinbase.wallet.client import Client
import Extracting_Credentials as EC
import json


file_Path="/Users/louisfuture/Documents/coinbase_Key/Key.json"


Api_Key, Api_Secret = EC.Extract_Credentials(file_Path=file_Path)



#connect Get client information 
client = Client(Api_Key, Api_Secret)


#Primary account information

account = client.get_primary_account()

#print(account)


transactions = client.get_transactions("775db2ac-bba0-5b1c-8077-2972962d3633")



json_object = json.dumps(transactions, indent=4)

with open("Transaction.json", 'w') as outfile:
    outfile.write(json_object)