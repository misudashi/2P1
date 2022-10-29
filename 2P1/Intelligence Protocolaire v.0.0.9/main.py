import defs
import run
import src.config as config

defs.initialiser()
defs.talk("Bonjour, " + config.prénom + ", que puis-je faire pour vous ?")
while True:
    
    run.scripte()