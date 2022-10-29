from pystyle import Colors
from pythonping import ping
import USER_TOKEN as usr_token


if usr_token.TOKEN == "Bhf06d1ylaIVxnSYaBk23ukLAhXU8TCd":

    prénom = "Maître Erwan"
    CustomerColor = Colors.yellow_to_green
    AIColor = Colors.green_to_cyan
    NotesColor = Colors.rainbow
    GooglePing = ping('8.8.8.8')
    erreurCount = 0

elif usr_token.TOKEN == "jkqHXtdNJxLITT2nHgEAOyo6r8hhYMGT":

    prénom = "Maître Erwan ( VERSION DEBUG )"
    CustomerColor = Colors.yellow_to_green
    AIColor = Colors.green_to_cyan
    NotesColor = Colors.rainbow
    GooglePing = ping('8.8.8.8')
    erreurCount = 100

else:
    print("Merci d'entrer un TOKEN valide dans le fichier 'USER_TOKEN.py'.")
    exit()