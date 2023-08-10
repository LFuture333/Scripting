import datetime

while True:
    Now_Time = datetime.datetime.now()
    opening_Time = Now_Time.replace(hour=9, minute=30,second=15, microsecond=0,)
    if (Now_Time <= opening_Time):
        print("Market is open")

    else:
        print(Now_Time);