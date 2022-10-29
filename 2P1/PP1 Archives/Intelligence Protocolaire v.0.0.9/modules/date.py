import datetime
from main import command, talk

def giving_date():

    if "quel jour" in command:
        date = datetime.datetime.now().strftime("%D")
        time = datetime.datetime.now().strftime('%I:%M')
        talk("Nous sommes le " + date + " et il est " + time + ".")