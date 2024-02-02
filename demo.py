from random import *

from easygui import *

def angelinaGreeting():
    #define the title of the box, the msg it shows, and the choices in buttons
    title = "Angelina, Triton (she/her):"
    msg = "Will you deliver this letter?\nIt has to get to the Mayor TONIGHT!"
    choice = ['Yes!', 'No.']

    user = choicebox(msg,title,choice)

    msg2 = ("Thank you! I trust you do do this VERY DANGEROUS thing!!!\n"
            "The Mayor's office is in the *Aquamarine District*, hurry!")

    if user == 'Yes!':
        msgbox(msg2,title)
    elif user == 'No.':
        msgbox('No! We need your help please! Do it for the people of Neptune!',title)
        angelinaGreeting()

def firstRoom():
    angelinaGreeting()

firstRoom()
