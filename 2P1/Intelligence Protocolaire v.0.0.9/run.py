import src.modules.exiter as exiter
import src.modules.jouer as jouer
import src.modules.heure as heure
import src.modules.qui as qui
import src.modules.internetsearch as searchlo
import src.modules.blague as blague
import src.modules.prefere as fav
import src.modules.ca_va as humeur
import src.modules.politesse as hello_there
import src.modules.remerciements as merciquoi
import src.modules.cdc as cdc
import src.modules.oui as oui
import src.modules.sinon as sinon
import src.modules.pswrd as mdp
import src.modules.moviefinder as cinematographie
import src.modules.datation as dateu
import src.modules.calcu as calcu
import defs as defs
import src.config as config
import src.string_list as listing


import pywhatkit
from pystyle import Write, Colors
import wikipedia
import pyperclip as pc
try:
    from googlesearch import search
except ImportError:
    defs.talk("Je n'ai pas trouvé de module nommé Google !")

wikipedia.set_lang("fr")



# à chaque fois que le module utilise la variable command, le développer ici.

def scripte():

    command = defs.take_command()
    command = str(command)


    if 'exit' in command:
        exiter.exiting()



    elif 'joue' in command:
        if 'youtube' in command:
            defs.talk(jouer.playingursong + command + '".')
            song = command.replace('joue', '')
            song = song.replace('youtube', '')
            pywhatkit.playonyt(song)
        else: 
            defs.talk(jouer.jpp)



    elif 'heure' in command:
        heure.heure()

    elif 'jour' in command or 'date' in command:
        dateu.datage()



    elif 'qui' in command:
        if 'est' in command:
            person = command.replace('qui', '')
            person = person.replace("est", "")
            try:
                info = wikipedia.summary(person, 1)
                defs.talk(info)
            except:
                defs.talk(qui.nof)
                for inform in search(person, tld="co.in", num=10, stop=5, pause=2):
                    defs.talkprint(inform)
                
        else:
            defs.talk(qui.rien)



    elif 'cherche' in command:
        if 'internet' in command: 
            subject = command.replace("cherche", "")
            subject = subject.replace("internet", "")
            subject = subject.replace("cherche sur", "")
            subject = subject.replace("sur internet", "")
            subject = subject.replace("recherche", "")
            #defs.talk(searchlo.subjecting)
            #r = Write.Input(text=config.prénom + " => ", color=config.CustomerColor, interval=0.005)
            if subject != "": # if r !=        :-)
                try: 
                    info = wikipedia.summary(subject, 3)
                    defs.talk(info)
                except:
                    defs.talk(searchlo.nof)
                    for inform in search(person, tld="co.in", num=10, stop=10, pause=2):
                        defs.talkprint(inform)
            else: 
                info = searchlo.plzenter
                defs.talk(info)
        else: 
            info = searchlo.moitie
            defs.talk(info)


            
    elif 'blague' in command:
        defs.talk("Je rencontre un petit problème avec le système de blagues actuellement")



    elif 'trouve' in command:
        if 'film' in command or 'série' in command:
            command = command.replace("le film" , "")
            command = command.replace("film", "")
            command = command.replace("la série" , "")
            command = command.replace("série" , "")
            command = command.replace("trouve" , "")
            movie_name = command
            defs.talk("Je recherche actuellement le film " + movie_name + " dans les bases de données de Google Drive: ")
            movie_link = cinematographie.search(movie_name=movie_name)
            if movie_link:
                defs.talk("Voici le lien de votre film: ")
                defs.talkprint(movie_link)
                defs.talk("\nAppuyez sur Entrée pour copier le lien sur votre presse-papier :")
                defs.talkinput("=> ")
                pc.copy(movie_link)
            else:
                defs.talk("Je suis désolé, mais je n'ai rien trouvé dans les bases de données de Google Drive !")
                return



    elif 'préféré' in command or 'prefere' in command or 'préfère' in command:
        if 'livre' in command:
            defs.talk(fav.livreu + listing.favourite["book"])
        elif 'film' in command:
            defs.talk(fav.filmeu + listing.favourite["movie"])
        elif 'série' in command:
            defs.talk(fav.serieu + listing.favourite["movie"])
        elif 'jeu' in command:
            defs.talk(fav.jeuu + listing.favourite["video game"])
        else:
            defs.talk(fav.unfoundpref)



    elif 'identifiant' in command or 'mot de pass' in command:
        if 'discord' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.discordID["mail"] + " ; " + listing.discordID["password"] + " ; \n\nAlternative(s) : " + listing.discordID["alternative"])
        if 'plesk' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.pleskID["name"] + " ; " + listing.pleskID["password"])
        if 'twitter' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.twitterID["mail"] + " ; " + listing.twitterID["password"])
        if 'ecole direct' in command or 'ecoledirect' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.ecoledirecteID["mail"] + " ; " + listing.ecoledirecteID["password"] + " ; " + listing.ecoledirecteID["name"])
        if 'heroku' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.herokuID["password"])
        if 'mediafire' in command or 'media fire' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.mediafireID["mail"] + " ; " + listing.mediafireID["password"])
        if 'minecraft' in command or 'mc' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.minecraftID["mail"] + " ; " + listing.minecraftID["password"])
        if 'osu' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.osuID["name"] + " ; " + listing.osuID["password"])
        if 'sitedudev' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.sitedudevID["mail"] + " ; " + listing.sitedudevID["password"])
        if 'github' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.githubID["mail"] + " ; " + listing.githubID["password"])
        if 'twitch' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.twitchID["mail"] + " ; " + listing.twitchID["password"] + " ; " + listing.twitchID["name"])
        if 'yahoo' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.yahooID["mail"] + " ; " + listing.yahooID["password"] + " ; \n\nAlternative(s) : " + listing.yahooID["alternative"])
        if 'spotify' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.spotifyID["mail"] + " ; " + listing.spotifyID["password"])
        if 'wattpad' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.wattpadID["mail"] + " ; " + listing.wattpadID["password"] + " ; " + listing.wattpadID["name"])
        if 'steam' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.steamID["mail"] + " ; " + listing.steamID["password"] + " ; " + listing.steamID["name"])
        if 'pix' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.pixID["name"] + " ; " + listing.pixID["password"])
        if 'hideme' in command or 'hide.me' in command or 'hide me' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.hidemeID["mail"] + " ; " + listing.hidemeID["password"] + " ; " + listing.hidemeID["name"])
        if 'carddco' in command or 'card.co' in command or 'card co' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.carddcoID["mail"] + " ; " + listing.carddcoID["password"] + " ; " + listing.carddcoID["name"])
        if 'tutanota' in command or 'mail trash' in command:
            defs.talk(mdp.found)
            defs.talkprint(listing.tutanotaID["mail"] + " ; " + listing.tutanotaID["password"] + " ; " + listing.tutanotaID["name"])

    
    elif 'calcul' in command:
        defs.talk(calcu.enterpls)
        c = Write.Input(text="=> ", color=config.AIColor, interval=0.005)
        c = str(c)
        if '1' in c or 'ddition' in c:
            defs.talk(calcu.qq + "ajouter ?")
            x = defs.talkinput("=> ")
            defs.talk(calcu.tb + "ajouter ?")
            y = defs.talkinput("=> ")
            r = calcu.add(int(x) , int(y))
            defs.talk(calcu.res + str(r))
        elif '2' in c or 'oustraction' in c:
            defs.talk(calcu.qq + "soustraire ?")
            x = defs.talkinput("=> ")
            defs.talk(calcu.tb + "soustraire ?")
            y = defs.talkinput("=> ")
            r = calcu.subtract(int(x) , int(y))
            defs.talk(calcu.res + str(r))
        elif '3' in c or 'ultiplication' in c:
            defs.talk(calcu.qq + "multiplier ?")
            x = defs.talkinput("=> ")
            defs.talk(calcu.tb + "multiplier ?")
            y = defs.talkinput("=> ")
            r = calcu.multiply(int(x) , int(y))
            defs.talk(calcu.res + str(r))
        elif '4' in c or 'ivision' in c:
            defs.talk(calcu.qq + "diviser ?")
            x = defs.talkinput("=> ")
            defs.talk(calcu.tb + "diviser ?")
            y = defs.talkinput("=> ")
            r = calcu.divide(int(x) , int(y))
            defs.talk(calcu.res + str(r))
        else:
            defs.talk(calcu.erreure)


    elif 'ça va' in command:
        humeur.commentcavabien()



    elif 'salut' in command or 'bonjour' in command or 'hey' in command or 'yo' in command:
        hello_there.bonjoureuh()



    elif 'merci' in command or 'cimer' in command:
        merciquoi.mercienft()



    elif command == "cdc":
        defs.talk("Voici mon cahier des charges: ")
        cdc.cahierdeschargesCDC()



    elif command == 'oui':
        oui.ouimdr()

        

    else:
        sinon.sinonnonnon()