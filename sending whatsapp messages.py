from datetime import datetime

import emoji
import pywhatkit
from emoji import emojize
print(emojize(":thumbs_up:"))
print(emoji.emojize(":partying_face:"))
now = datetime.now()
pywhatkit.sendwhatmsg('+94717405579', " Hey wish you a happy birthday!",int(now.strftime("%H")), int(now.strftime("%M"))+1,15, True, 2)
pywhatkit.sendwhatmsg('+94717405579', emojize(":partying_face:"),int(now.strftime("%H")), int(now.strftime("%M"))+2, 30, True, 2)