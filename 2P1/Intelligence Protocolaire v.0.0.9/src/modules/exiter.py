import defs
import src.config as config

def exiting():
    defs.talk("Ce fut un plaisir " + config.prénom + ".")
    exit()
    