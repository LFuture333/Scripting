from coinbase.wallet.client import Client

import Extracting_Credentials as EC


file_Path="/Users/louisfuture/Documents/coinbase_Key/Key.json"


Api_Key, Api_Secret = EC.Extract_Credentials(file_Path)





client = Client(api_key=Api_Key, api_secret=Api_Secret)


print(" Get Accounts \n")
print(client.get_accounts())


print("Get Primary Account \n")

print(client.get_primary_account())