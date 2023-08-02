#all this data will be extracted from fidelity website (using selenium )
Accounts_Name=['Portfolio_1', 'Portfolio_2']
Total_Account_Value = [250.00, 145.20]
Cash_Available_Trade = [240.00, 100.00]
Availavle_Withdraw = [10.00, 45.20]



#This tuple hold all accoun information
Accounts_tuple=[]


for i, account in enumerate(Accounts_Name):
    # Create a list for the current account 
    current_account = [(account,
                          Total_Account_Value[i],
                          Cash_Available_Trade[i],
                          Availavle_Withdraw[i])]
    

    #Append all account information to the tuple account 
    Accounts_tuple.append(current_account)


print("Account Tuple example")
print(Accounts_tuple)