from pystyle import System, Colorate, Center, Anime, Write
import src.ascii as ascii
import src.config as config
import src.string_list as listing
import USER_TOKEN as usr_token
import pyttsx3
engine = pyttsx3.init()



def initialiser():

    System.Clear()
    System.Size(160, 50)
    System.Title("Programme Protocolaire 1 (2P1) Version 0.0.9")
    Anime.Fade(text=Center.Center(ascii.banner), color=config.CustomerColor, mode=Colorate.Vertical, enter=True)
    print('\n'*2)
    print(Colorate.Diagonal(color=config.CustomerColor, text=Center.XCenter(ascii.ascii_art)))
    print('\n'*3)
    print(Colorate.Diagonal(color=config.AIColor, text=Center.XCenter("Connexion en utilisant le Token '" + usr_token.TOKEN + "'")))
    print('\n'*3)
    print(Colorate.Diagonal(color=config.AIColor, text=Center.XCenter("|-----------------------------------------------------------------------------------------------------------------------|\n"))) #Barre de chargement
    print('\n'*3)

def take_command(): 

    try:
            command = Write.Input(text="\n" + config.prénom + " => ", color=config.CustomerColor, interval=0.005)
            command = command.lower()
            if 'programme protocolaire' in command:
                command = command.replace('programme protocolaire', '')
            if "2p1" in command:
                command = command.replace("2p1", "")   
    except:
        pass
    return(command)

def talk(text): 

    print(Colorate.Diagonal(color=config.AIColor, text="\n2P1 => " + text + "\n\n"))
    #engine.say(text)
    #engine.runAndWait()
def talkprint(text):

    print(Colorate.Diagonal(color=config.AIColor, text="\n2P1 => " + text + "\n\n"))
def talkinput(text):

    rsi = Write.Input(text=text, color=config.AIColor, interval=0.005)
    return rsi
    

