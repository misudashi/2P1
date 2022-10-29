import defs
import src.config as config
import src.string_list as listing

import pythonping

def commentcavabien():

    response_list = pythonping.ping('8.8.8.8', size=40, count=10)
    GooglePing = response_list.rtt_avg_ms
    emotionalState = "Tout semble normal"
    if config.erreurCount != 0:
        emotionalState = "J'ai précisément " + str(config.erreurCount) + " erreurs. Je ne sais pas d'où elles viennent, mais elles ne semblent pas perturber mon cours de fonction de 'survie' !"
        defs.talk(emotionalState)
    else: 
        defs.talk("Je ne détecte aucune erreur.")


    if GooglePing > 200:
        defs.talk("Disons que je pourrais aller mieux. Ma connexion Internet a une latence d'environ " + str(GooglePing) + "ms")
    else:
        defs.talk("J'ai actuellement un ping de " + str(GooglePing) + "ms !")