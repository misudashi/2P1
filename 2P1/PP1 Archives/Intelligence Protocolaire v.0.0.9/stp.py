import datetime
import random

import pyjokes
import pywhatkit
import wikipedia
from pystyle import Anime, Center, Colorate, System, Write
from pythonping import ping

from src.config import AIColor, CustomerColor, prénom
from src.ascii import ascii_art, banner
from src.string_list import favourite, hi_list

wikipedia.set_lang("fr")


def talk(text): 

    print(Colorate.Diagonal(color=AIColor, text="\n2P1 => " + text + "\n\n"))

def take_command(): 

    try:
            command = Write.Input(text="\n" + prénom + " => ", color=CustomerColor, interval=0.005)
            command = command.lower()
            if 'programme protocolaire' in command:
                command = command.replace('programme protocolaire', '')
            if "2p1" in command:
                command = command.replace("2p1", "")   
    except:
        pass
    return(command)

def init():

    System.Clear()
    System.Size(160, 50)
    System.Title("Programme Protocolaire 1 (2P1) Version 0.0.8")
    Anime.Fade(text=Center.Center(banner), color=CustomerColor, mode=Colorate.Vertical, enter=True)
    print('\n'*2)
    print(Colorate.Diagonal(color=CustomerColor, text=Center.XCenter(ascii_art))) #LOGO DE 2P1
    print('\n'*3)
    print(Colorate.Diagonal(color=AIColor, text=Center.XCenter("|-----------------------------------------------------------------------------------------------------------------------|\n"))) #Barre de chargement
    print('\n'*3)
    print(Colorate.Diagonal(color=AIColor, text="2P1 => Bonjour, " + prénom + ". Que puis-je faire pour vous ?\n\n"))

