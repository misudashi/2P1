import defs

import datetime

def datage(): 
    time = datetime.datetime.now().strftime('%d/%m/%Y')
    defs.talk("Aujourd'hui, nous sommes le " + time)