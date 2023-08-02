import json 

def Demo(file_path):

    #Memory allocation for (USERNAME & PASSWORD)
    Usernames = []
    Passwords = []

# Open the json file 
    f = open(file_path);
    
    #Extract the data from the file 
    data = json.load(f)

#Extract all the data from the account section one by one 
    for i in data["MyAccount"]:
        credentials = list(i.values())

        #store each individual value in the coresponding list (Password for passwords & Username for Usenames )
        Usernames.append(credentials[0])
        Passwords.append(credentials[1])


# Print store values one by one with the position of them in the list 
    for t in range(len(Passwords)):
        print(str(t)+ ") " + str(Usernames[t]))               
    

    #username & Password selected by User input (memory)
    Username=""
    Password=""

#Entering loop to recive user selection
    while (True):

        #input selction of use  
        selection_user = int(input("Select the user that you want to use: "))

    # If the input enter by user not in range (program stays in loop)
        if(int(selection_user) > len(Usernames)):
            print("that user is not in credentials.json file")

    # If the input enter is in range of list the program will return the value and exit
        if(int(selection_user) < len(Usernames)):
            print("the Account selected was: " + str(Usernames[int(selection_user)]))

            Username= Usernames[int(selection_user)]
            Password = Passwords[int(selection_user)]

            break
    
    return(Username, Password)

Username, Password = Demo(file_path="credentials.json")

