from coinbase.wallet.client import Client
import json

file_Path ="/Users/louisfuture/Documents/coinbase_Key/Key.json"

#Extract the credentials from the json file 
def Extract_Credentials(file_Path):

    #Memory allocation for (Api_Key   & Api_Secret)
    Api_Keys = []
    Api_Secrets = []

# Open the json file 
    f = open(file_Path);
    
    #Extract the data from the file 
    data = json.load(f)

#Extract all the data from the account section one by one 
    for i in data["Account"]:
        credentials = list(i.values())

        #store each individual value in the coresponding list (Api_Secret for Api_Secrets & Api_Key   for Usenames )
        Api_Keys.append(credentials[0])
        Api_Secrets.append(credentials[1])


# Print store values one by one with the position of them in the list 
    for t in range(len(Api_Secrets)):
        print(str(t)+ ") " + str(Api_Keys[t]))               
    

    #Api_Key & Api_Secret selected by User input (memory)
    Api_Key = ""
    Api_Secret = ""

#Entering loop to recive user selection
    while (True):

        #input selction of use  
        selection_user = int(input("Select the user that you want to use: "))

    # If the input enter by user not in range (program stays in loop)
        if(int(selection_user) > len(Api_Keys)):
            print("that user is not in credentials.json file")

    # If the input enter is in range of list the program will return the value and exit
        if(int(selection_user) < len(Api_Keys)):
            print("the Account selected was: " + str(Api_Keys[int(selection_user)]))

            Api_Key =  Api_Keys[int(selection_user)]
            Api_Secret = Api_Secrets[int(selection_user)]

            break
    
    return(Api_Key, Api_Secret)


Api_Key, Api_Secret = Extract_Credentials(file_Path=file_Path)

client = Client(api_key=Api_Key, api_secret=Api_Secret)


#Account information 
user = client.get_current_user()
user_as_json_string = json.dumps(user)

print(user_as_json_string)



print("Get Currencies \n")

print(client.get_currencies())


print(" Get Accounts \n")
print(client.get_accounts())


print("Get Primary Account \n")

print(client.get_primary_account())