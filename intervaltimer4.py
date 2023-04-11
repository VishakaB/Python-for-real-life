import datetime
import winsound
import tkinter as tk
import os
import time

# Define the interval time in five minutes
interval = 5
instance = 0

def set_target_time():
    instance = 0
    #current time
    current_time = datetime.datetime.now()

    # Calculate the next multiple of the interval time
    minute = current_time.minute
    if minute % interval != 0:
        minute = ((minute // interval) + 1) * interval
    if minute == 60:
        minute = 0
        current_time += datetime.timedelta(hours=1)

    # Set the target time
    target_time = current_time.replace(minute=minute, second=0, microsecond=0)
    return target_time

def check_time():
    # Get the current time and target time
    current_time = datetime.datetime.now()
    target_time = set_target_time()

    instance = 0
    # Check if it's time to switch
    if  current_time >= target_time:
        # Play the sound
        #winsound.PlaySound("C:\\Users\\visha\\OneDrive\\Desktop\\Ding Ding Iphone.mp3", winsound.SND_FILENAME)

        if instance < 1:
            os.startfile(r"C:\Users\visha\OneDrive\Desktop\Ding Ding Iphone.mp3")
            blink(60)
            time.sleep(60)

        # Update the target time
        target_time = set_target_time()
    instance = 0

    # Update the label
    time_label.config(text=current_time.strftime("%H:%M:%S"))

    # Schedule the next check
    time_label.after(1000, check_time)

def blink():
    time_label.config(bg="red")
    time_label.after(500, lambda: time_label.config(bg=window.cget("bg")))

# Create the tkinter window
window = tk.Tk()
window.title("Interval Timer")

# Create the time label
time_label = tk.Label(window, font=("Arial", 50))
time_label.pack()

# Start the timer
check_time()

# Run the window
window.mainloop()