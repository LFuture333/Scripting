import time

range_1 = range(9, 16)

num = int(time.strftime("%H"))
minutes = 45

num_opening = 9

if (num in range_1):
    print(num)
    

    opening_market = range(30, 59)


#This if statement detects if the market is open (specific for (9 hr)  Range of minutes from (30 , 59) )
    if( (num_opening <= 9) and (  minutes in opening_market)):
        print("market is open")



# market closes at 16:00 Anything over 15:59 (Calls for no more execution ( Declare market has close))