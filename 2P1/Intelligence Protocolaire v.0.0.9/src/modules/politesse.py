import defs
import src.config as config
import src.string_list as listing

import random

def bonjoureuh():
    randomHi = random.choice(listing.hi_list)
    defs.talk(randomHi + ", " + config.prénom + ". Auriez-vous une quelconque requête à mon égard ?")