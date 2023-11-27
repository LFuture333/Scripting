import json

file_Path="/Users/louisfuture/Documents/coinbase_Key/Key.json"



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




    #Api_Key & Api_Secret selected by User input (memory)
    Api_Key = ""
    Api_Secret = ""
    if (len(Api_Keys) == 1 ):
        Api_Key = (Api_Keys[0])
        Api_Secret = (Api_Secrets[0])
        
        return(Api_Key, Api_Secret)

    else:


    #Entering loop to recive user selection
        while (True):

            # Print store values one by one with the position of them in the list 
            for t in range(len(Api_Secrets)):
                print(str(t)+ ") " + str(Api_Keys[t]))               
    
            #input selction of use
            selection_user = int(input("Select the user that you want to use: "))    

        #If the input enter by user not in range (program stays in loop)
            if(int(selection_user) > len(Api_Keys)):
                print("That user is out of range")
        
        
        # If the input enter is in range of list the program will return the value and exit
            if(int(selection_user) < len(Api_Keys)):
                print("the Account selected was: " + str(Api_Keys[int(selection_user)]))

                Api_Key= Api_Keys[int(selection_user)]
                Api_Secret = Api_Secrets[int(selection_user)]

            break

    return(Api_Key, Api_Secret)

