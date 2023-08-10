import time

Market_Open = "9:30"

Market_Closing = "16:00"

while True:
    # Current time At the moment of call 
    hour = 9
    Minute = 12

#Detect the time from (9:30 Forward) The market is open
    if ((int(hour) >= 9)):
        if (int(Minute) in range(00, 59)):
            print ("Market open")

# Detect the Time of (0:00 to 9:29) The market is close
    if ((int(hour) <= 9) and  (int(Minute) <= 29)):
        print("Market Close")





# Time of the market opening  
        #9:30 To 16:00 