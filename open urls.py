import webbrowser

#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#webbrowser.get(chrome_path).open('http://docs.python.org/')
#google calendar
webbrowser.open('https://calendar.google.com/calendar/u/0/r/customday?tab=rc')

#research completion
webbrowser.open('https://docs.google.com/spreadsheets/d/1og_Qr-Om9FoCMRTYdGcFbSUCFz2GsAQf2T_0gPd8vYg/edit#gid=798295092')

#overleaf current project
webbrowser.open('https://www.overleaf.com/project/627cdf2ef895beaabef1da74')

#powerpoint ppt asynchronous noma
webbrowser.open('https://docs.google.com/presentation/d/1BDk18QT_5R4oF9s5TVuxndYTlZw4eOB2DlCd3PDCTa0/edit#slide=id.g128700276ab_0_0')

#website #optional
webbrowser.open('https://editor.wix.com/html/editor/web/renderer/edit/0a76b43a-90c4-49f2-894f-73f8aa8b02e1?_gl=...'
                '1*1qgquke*_ga*MjA0NzI0NjAyMi4xNjQ5NTUxMzc0*_ga_H314XQHSPY*MTY1MDQ0Mjg1Ny4xLjEuMTY1MDQ0Mjg5NS4yMg..&editorSessionId...'
                '=8dcf8a9c-dbfe-48a7-90fa-f46ab3245578&metaSiteId=43a93ec4-6178-467c-a727-743aaa60e165')

#tech with tim youtube
webbrowser.open('https://www.youtube.com/c/TechWithTim')

#good mythical morning
webbrowser.open('https://www.youtube.com/GoodMythicalMorning')

#opn pdfs
#pdf 1
webbrowser.open_new(r'file://C:\Users\visha\OneDrive\Desktop\most read pdfs\special_transactions_wirelessv2.pdf')
#pdf 2
webbrowser.open_new(r'file://C:\Users\visha\OneDrive\Desktop\most read pdfs\wireless_binary_opti2.pdf')
#pdf 3
webbrowser.open_new(r'file://C:\Users\visha\OneDrive\Desktop\most read pdfs\wireless_binary_opti3.pdf')
#pdf 4
webbrowser.open_new(r'file://C:\Users\visha\OneDrive\Desktop\most read pdfs\1.Energy Efficiency Optimization for NOMA.pdf')

#open matlab
import os
os.startfile(r'C:\Program Files\Polyspace\R2021a\bin\matlab.exe')

#open pycharm
import os
os.startfile(r'C:\Program Files\JetBrains\PyCharm Community Edition 2021.3\bin\pycharm64.exe')


#date: 22 May 2022
#ref:https://github.com/thedreamcode/python_basics/blob/master/read_video_audio.py

import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer


def getVideoSource(source, width, height):
    cap = cv2.VideoCapture(source)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    return cap


def running_videos(sourcePath):
    #sourcePath = r"C:\Users\visha\OneDrive\Desktop\1.mp4"
    camera = getVideoSource(sourcePath, 720, 480)
    player = MediaPlayer(sourcePath)

    while True:

        ret, frame = camera.read()
        audio_frame, val = player.get_frame()

        if (ret == 0):
            print("End of video")
            break

        frame = cv2.resize(frame, (720, 480))
        cv2.imshow('Camera', frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

        #if val != 'eof' and audio_frame is not None:
            #frame, t = audio_frame
            #print("Frame:" + str(frame) + " T: " + str(t))

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    running_videos( r"C:\Users\visha\OneDrive\Desktop\1.mp4")
    running_videos(r"C:\Users\visha\OneDrive\Desktop\dhammanupassana\most watched\garyvee\..."
                   r"Your Problems Don't Matter, Here's Why _ Talk at the Precious Dreams Foundation.mp4")