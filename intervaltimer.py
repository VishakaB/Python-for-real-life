
from tkinter import *
import datetime
import time
import winsound
import os

#find the current time
current_time = datetime.datetime.now()
now = current_time.strftime("%H:%M:%S")
date = current_time.strftime("%d/%m/%Y")
datem = datetime.datetime.strptime(now, "%H:%M:%S")

#set preferred interval
interval = 5

#loop initiation
loop = False

#intermediate variable
y = datem.minute
#set the target time to next fifth multiple of minutes
if datem.minute%interval != 0:
   y = (datem.minute//interval)*interval

#initialization
h = str(datem.hour)
m = str(y + interval)
s = "00"
# if hour is below 10, add a zero infront to bring the hour to standard
if datem.hour < 10:
    h = "0" + str(datem.hour)
    m = str(y + interval)
    s = "00"
#increase the hour by one when minutes are higher than 55
if y >= 55:
    h = str(datem.hour+1)
    m = "00"
    s = "00"
if y >= 55 & datem.hour >= 23:  # when hour passes 23h mark it should be set to 00
    h = "00"
    m = "00"
    s = "00"
# if minute is below 10, add a zero infront to bring the minute to standard
if y + interval < 10:
    #hour has been set in earlier cases as suitably
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

        h = str(datem.hour)
        m = str(datem.minute+interval)
        s = "00"
        if datem.hour < 10:
            h = "0"+str(datem.hour)
        # when minutes reach 55, the addition must be equal to 00 and hours must be up by one
        if datem.minute == 55:
            h = str(datem.hour+1)
            m = "00"
        if  datem.hour < 10 & datem.minute == 55:
            h = "0" + str(datem.hour+1)
            m = "00"
        if datem.minute == 55 & datem.hour >= 23: #when hour passes 23h mark it should be set to 00
            h = "00"
            m = "00"
        if datem.minute + interval < 10:
            h = "00"
            m = "0" + str(datem.minute + interval)

        target_str = h + ":" + m + ":" + s
        print(target_str)

        loop = False  # return to loop
    else:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        loop= False


