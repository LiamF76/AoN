from random import *

from easygui import *

def angelinaGreeting():
    title = "Angelina, Triton (she/her):"
    msg = "Will you deliver this letter?\nIt has to get to the Mayor TONIGHT!"
    choice = ['Yes!', 'No.']

    user = buttonbox(msg,title,choice)

    msg2 = "Thank you! I trust you do do this VERY DANGEROUS thing!!!"

    if user == 'Yes!':
        msgbox(msg2,title)
    else:
        msgbox('wtf bro',title)

def firstRoom():
    angelinaGreeting()

firstRoom()
