import defs

import pyjokes

def blaguage():
    xx = pyjokes.get_joke(language="fr", category="all")
    defs.talk(xx)