

import datetime
import random


import pyjokes
import pywhatkit
import wikipedia
from pystyle import Anime, Center, Colorate, System, Write
from pythonping import ping

from init import *

wikipedia.set_lang("fr")


erreurCount = 0
ra = [1, 2, 3, 4, 5, 6, 7, 8, 9]



def run():
    print("1")
    
    print("2")
    randomHi = random.choice(hi_list)

    giving_date()

    if 'exit' in command:
        talk("Ce fut un plaisir " + prénom + ".")
        exit()

    if 'joue' in command:
        if 'youtube' in command:
            talk('Je joue actuellement votre requête "' + command + '".')
            song = command.replace('joue', '')
            pywhatkit.playonyt(song)
        else: talk("Voulez-vous que je joue sur YouTube votre musique? Merci de me l'indiquer dans la commande.")

    elif 'heure' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Il est actuellement ' + time)



    elif 'qui' in command:
        if 'est' in command:
            person = command.replace('qui', '')
            person = person.replace("est", "")
            info = wikipedia.summary(person, 1)
            talk(info)
        else: 
            talk("Voulez-vous que je recherche sur Internet une personnalité publique ? Merci de l'indiquer en utilisant la formule 'qui est' par exemple.")

    elif 'cherche' in command:
        if 'internet' in command: 
            subject = command.replace("cherche", "")
            subject = subject.replace("internet", "")
            talk('Veuillez indiquer le sujet de votre recherche:\n')
            r = Write.Input(text=prénom + " => ", color=CustomerColor, interval=0.005)
            if r != "":
                info = wikipedia.summary(r, 5)
            else: 
                info = "Veuillez entrer un sujet !"
            talk(info)
            
        else: talk("Voulez-vous que je fasse une recherche Internet sur ce sujet ? Merci de l'indiquer en utilisant la formule 'cherche <sujet> sur Internet' par exemple.")

    elif 'blague' in command:
        talk("Malheureusement, je ne suis capable que de dire des blagues en Anglais pour l'instant. J'espère que vous la comprendrez: " + '"' + pyjokes.get_joke() + '"')
    elif 'préféré' in command:
        if 'livre' in command:
            talk("Mon livre préféré est " + favourite["book"])
        elif 'film' in command:
            talk("Mon film préféré est " + favourite["movie"])
        elif 'série' in command:
            talk("Mon film préféré est " + favourite["movie"])
        elif 'jeu' in command:
            talk("Mon jeux préféré est " + favourite["video game"])
        else:
            talk("Je n'ai pas vraiment de préférences à ce sujet.. Mais vous pouvez me faire part de vos goûts personnels !")
    elif 'ça va' in command:
        response_list = ping('8.8.8.8', size=40, count=10)
        GooglePing = response_list.rtt_avg_ms
        emotionalState = "Tout semble normal"
        if erreurCount != 0:
            emotionalState = "J'ai précisément " + str(erreurCount) + " erreurs. Je ne sais pas d'où elles viennent, mais elles ne semblent pas perturber mon cours de fonction de 'survie' !"
            talk(emotionalState)
        else: 
             talk("Je ne détecte aucune erreur.")

        if GooglePing > 200:
            talk("Disons que je pourrais aller mieux. Ma connexion Internet a une latence d'environ " + str(GooglePing) + "ms")
        else:
            talk("J'ai actuellement un ping de " + str(GooglePing) + "ms !")
        
    elif 'salut' in command:
        talk(randomHi + ", " + prénom + ". Auriez-vous une quelconque requête à mon égard ?")
        randomHiN = random.choice(ra)
    
    elif 'bonjour' in command:
        talk(randomHi + ", " + prénom + ". Auriez-vous une quelconque requête à mon égard ?")
        randomHiN = random.choice(ra)

    elif 'hey' in command:
        talk(randomHi + ", " + prénom + ". Auriez-vous une quelconque requête à mon égard ?")
        randomHiN = random.choice(ra)

    elif 'yo' in command:
        talk(randomHi + ", " + prénom + ". Auriez-vous une quelconque requête à mon égard ?")
        randomHiN = random.choice(ra)
    
    
    elif 'merci' in command:
        talk("Pas de problème, " + prénom + " !")
    
    elif command == "cdc":
        print(Colorate.Diagonal(color=NotesColor, text='Pour la 0.1.0: \n\n- Avoir une conversation très fluide et répondre à n' + "'importe quelle question\nChoses à implémenter: Etat d'émotion: " + '"ça va? comment vas-tu?" => ça va, mon programme m' + "'indique que je n'ai pas reçu d'erreur / j'ai reçu un message d'erreur provenant de la fonction <fonction>\nTraductions dans 20 langues\nOpérations: multiplications, additions, soustractions, etc complexes." + "\n\n\n\nPour la 1.0.0: \n\n- Augmenter son vocabulaire, varier ses réponses selon son humeur pour avoir la sensation de parler avec une personne normale.\n\n\nERREURS A CORRIGER: \n\nSteve Jones != Steve Jobs"))
    elif command == "oui":
        talk("Je vous écoute !")
    else:
        talk("Je n'ai pas bien compris. Merci de reformuler votre phrase. Si vous avez des suggestions pour m'améliorer, veuillez contact Misudashi: @misudashi sur Twitter.")


init()
while True:
    
    command = take_command
    from modules.date import giving_date
    run()
    
