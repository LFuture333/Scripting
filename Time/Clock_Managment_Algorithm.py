import time
        #   |9am|10am|11am|12pm|1pm|2pm|3pm|4pm|5pm|6pm| 7pm| 8pm| 9pm| 10pm| 11pm|12am| 1am|
current_h = [9,  10 , 11  ,12,  13, 14 ,15, 16, 17,  18,  19,  20,  21,  22,  23,   00,  1, 2, 3 , 4, 5, 6, 7, 8  ]

for t in range( len(current_h) ):

    H_result = current_h[t]*(2)


    for l in range(31):

        M_result = l * (5);

        print(str(H_result) + ':' + str(M_result))
        
    print("Breaking Point")