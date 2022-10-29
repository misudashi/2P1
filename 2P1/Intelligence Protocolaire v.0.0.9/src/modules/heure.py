import defs

import datetime

def heure(): 
    time = datetime.datetime.now().strftime('%I:%M')
    defs.talk('Il est actuellement ' + time)