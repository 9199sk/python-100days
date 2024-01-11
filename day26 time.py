#time with good morning sir
import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
# hour=int(input("enter hour"))
# print(hour)
name=input("enter your name:").title()
if(hour>=0 and hour<12):
    print("good morning ",name)
elif(hour>=12 and hour<=16):
    print("good afternoon ")
elif(hour>=17 and hour<24):
    print("good night ",name)