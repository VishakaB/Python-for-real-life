
from tkinter import *
import datetime
import time
import winsound
import os

#find the current time
current_time = datetime.datetime.now()
now = current_time.strftime("%H:%M:%S")
datem = datetime.datetime.strptime(now, "%H:%M:%S")

#set preferred interval
interval = 5

#loop initiation
loop = False

#intermediate variable
y = datem.minute
#set the target time to next multiple of 5 minutes
if datem.minute%interval != 0:
   y = (datem.minute//interval)*interval

#initialization
h = str(datem.hour)
m = str(y + interval)
s = "00"

# if hour is below 10, add a zero infront
# to bring the hour to standard
if datem.hour+1 < 10:#if time is 07:20
    h = "0" + str(datem.hour)
    m = str(y + interval)
    s = "00"
#increase the hour by one when minutes
# are higher than 55
if y >= (60-interval):#if time is 17:55
    h = str(datem.hour+1)
    m = "00"
    s = "00"
if y >= (60-interval) and datem.hour+1 < 10:#if time is 07:55
    print(y >= (60-interval))
    h = "0" + str(datem.hour+1)
    m = "00"
    s = "00"
if y >= (60-interval) and datem.hour >= 23:  # if time is 23:55
    h = "00"
    m = "00"
    s = "00"
# if minute is below 10, add a zero infront to bring the minute to standard
if y + interval < 10:#if time is 17:00
    m = "0"+ str(y + interval)
    s = "00"

target_str = h + ":" + m + ":" + s
print("1 here: ",target_str)

while loop==False:
    if now == target_str:
        print("Time to Switch")
        loop=True
        os.startfile(r"C:\Users\visha\OneDrive\Desktop\simple-countdown.mp3")

        #take the current time
        datem = datetime.datetime.strptime(now, "%H:%M:%S")

        target_str = str(datem.hour) + ":" + str(datem.minute + interval) + ":" + str(datem.second)

        h = str(datem.hour)#15
        m = str(datem.minute+interval)#35
        s = "00"
        if datem.hour < 10:#time is 07:00
            h = "0"+str(datem.hour)
        # when minutes reach 55, the addition must be equal to 00 and hours must be up by one
        if datem.minute == (60-interval):#time is 17:55
            h = str(datem.hour+1)
            m = "00"
        if datem.minute == (60-interval) and datem.hour < 9:#time is 07:55
            print('here 1')
            h = "0"+str(datem.hour+1)
            m = "00"
        if datem.minute == (60-interval) and datem.hour >= 23: #if time is 23:55
            h = "00"
            m = "00"
        if datem.minute + interval < 10: #if time is 17:00
            print('here 2')
            m = "0" + str(datem.minute + interval)

        target_str = h + ":" + m + ":" + s
        print(target_str)

        loop = False  # return to loop
    else:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        loop= False


