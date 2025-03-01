
"""
TO-DO:
New Hint function for guessing characters
Figure out how to continue the music after the minions scream
"""
'''DONE: 
create a function to tell you that you are wrong when you click the wrong character (Kind of like Checker for houses)
4 Houses, Gryffindor, Hufflepuff, Ravenclaw, Slytherin
10 Characters per house
Guess The House
Then The character
Use a random library to randomly choose a house, then a character from that house.
give a hint to the house, Hint= "It's an Animal."
Wrong = Litle Screen pops up
Right = ????????
Buttons at top of window for house guess
Small Screen for the house guess
'''
"""
CHARACTERS: 
GRYFFINDOR: Harry Potter, Hermione Granger, Ron Weasley, Neville Longbottom, Ginny Weasley, Fred Weasely, Albus Dumbledore, Lily Potter, James Potter, Sirius Black,

Hufflepuff: Cedric Diggory, Nymphadora Tonks, Pomona Sprout, Hannah Abbott, Ernie Macmillian, Susan Bones, Justin Finch-Fletchley, Mad Eye-Moody, Helga Hufflepuff, Zacharias Smith, 

Slytherin: Draco Malfoy, Severus Snape, Bellatrix Lestrange, Lord Voldemort, Blaise Zabini, Lucius Malfoy, Horace Slughorn, Marcus Flint, Gregory Goyle, Vincent Crabbe,

Ravenclaw: Luna Lovegood, Cho Chang, Moaning Myrtle, Gilderoy Lockhart, Rowena Ravenclaw, Filius Flitwick, Padma Patil, Professer Trelawney, Rowena Ravenclaw, Helena Ravenclaw,
"""
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import Label
from tkinter import simpledialog

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load("Sound/despicable-me-4-made-with-Voicemod.mp3")  # Replace with your file
pygame.mixer.music.play(-1)

#PREPARE
minion_sound = pygame.mixer.Sound("Sound/minions-screaming.mp3")
minion_sound.set_volume(3.8)  # Set volume 380%

def play_music():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)
play_music()
# Play minions screaming sound as a one-shot effect
def play_sound_effect(effect):
    effect.play()



# Wait for the sound to finish, then restart the background music
def resume_music():
    pygame.mixer.music.load("Sound/despicable-me-4-made-with-Voicemod.mp3")
    pygame.mixer.music.play(-1)

hint_popup = None  # Add this at the top of your script



#import pillow as pil

# Create a list of houses
Houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] #This is a variable called houses, that has the value of an Array which stores the different house names
#The variables Gryffindor, Hufflepuff, Slytherin, and Ravenclaw, which has the value of an Array, which stores the different Character names in their house
Gryffindor = [
    "Harry Potter", "Hermione Granger", "Ron Weasley", "Neville Longbottom",
    "Ginny Weasley", "Fred Weasely", "Albus Dumbledore", "Lily Potter",
    "James Potter", "Sirius Black"
]

Hufflepuff = [
    "Cedric Diggory", "Nymphadora Tonks", "Pomona Sprout", "Hannah Abbott",
    "Ernie Macmillian", "Susan Bones", "Justin Finch-Fletchley",
    "Mad Eye-Moody", "Helga Hufflepuff", "Zacharias Smith"
]

Slytherin = [
    "Draco Malfoy", "Severus Snape", "Bellatrix Lestrange", "Lord Voldemort",
    "Blaise Zabini", "Lucius Malfoy", "Horace Slughorn", "Marcus Flint",
    "Gregory Goyle", "Vincent Crabbe"
]

Ravenclaw = [
    "Luna Lovegood", "Cho Chang", "Moaning Myrtle", "Gilderoy Lockhart",
    "Rowena Ravenclaw", "Filius Flitwick", "Padma Patil",
    "Professer Trelawney", "Rowena Ravenclaw", "Helena Ravenclaw"
]
#From whatever the random house is, Random will randomyly select a character from the 10 in that house list

RandomHouses = random.choice(Houses)
if RandomHouses == "Gryffindor":
    RandomCharacter = random.choice(Gryffindor) #If the Random house is = to Gryffindor, the random character will be from the Gryffindor list
elif RandomHouses == "Ravenclaw":
    RandomCharacter = random.choice(Ravenclaw) #If the Random house is = to Ravenclaw, the random character will be from the Ravenclaw list
elif RandomHouses == "Slytherin":
    RandomCharacter = random.choice(Slytherin) #If the Random house is = to Slytherin, the random character will be from the Slytherin list
else:
    RandomCharacter = random.choice(Hufflepuff) #If the Random house is = to Hufflepuff, the random character will be from the Hufflepuff list
#This FUnction has a purpose which is to take in a string, check it with a list and then gives us the character list TFHAPWITTIASCIWAATGUTCL
def YUMYUMYUMHOUSESTRING(HS): #This method checks the house string with the character list from that house, and sends it to the button creator,
    # to create the buttons for the player to guess the character
    if HS == "Gryffindor":
        return Gryffindor
    elif HS == "Ravenclaw":
        return Ravenclaw
    elif HS == "Slytherin":
        return Slytherin
    else:
        return Hufflepuff
# CUSTOMIZTATION OF WINDOW/ Creates the guessing window
root = tk.Tk()
root.title("Guessing Window")
root.geometry("750x600")

WIDTH=1800
HEIGHT=1000



# HINT COMMAND
def Hint():
    #Creates a useless hint button, meant to trick the player
    hint = tk.Toplevel(root)
    hint.title("HINT: YOU'RE USELESS")
    hint.geometry("400x50")
    label = tk.Label(
        hint,
        text=
        "NO! Im not going around handing out hints \n deal with it yourself "
    )
    label.pack(pady=10)
    hint.resizable(False, False)


# HOMESCREEN
# Creates a hint label at the top of the screen, then has another label pop up to mildly infuriate the player,
# then calls the trick hint function
Homescreen = tk.Menu(root)
file_menu = tk.Menu(Homescreen, tearoff=0)
file_menu.add_command(
    label="Hah, This is to Annoy You",
    command=Hint,
)
Homescreen.add_cascade(label="Hint", menu=file_menu)
root.config(menu=Homescreen)
root.attributes("-fullscreen", True) #Makes it fullscreen

# Function to display a hint with the first letter of the character's name
def show_hint(event=None):
    first_letter = RandomCharacter[0]  # Get the first letter of the character's name
    hint_popup = tk.Toplevel(root)
    hint_popup.title("Hint")
    hint_popup.geometry("500x100")
    label = tk.Label(hint_popup, text=f"The character's name starts with: {first_letter}", font=("Comfortaa", 15))
    label.pack(pady=20) #Puts the first letter of the random character's name, into a hint
    hint_popup.resizable(False, False)

# Bind the 'h' key to the show_hint function
root.bind('h', show_hint)
#WE NEED TO ESCAPE, NO, DESTROY THIS MONSTROSITY WNTENDTM
def close_window():
    root.destroy()

#WE GOTTA LEAVE

exit_button = tk.Button(root, text="X",
command=close_window,
font=("Comfortaa",30),
bg="Red",
fg="Black")


exit_button.pack(pady=20)
exit_button.place(x=1860, y=0)


exit_button.pack(pady=20)
exit_button.place(x=1860, y=0)
# WINDOW That Pops up after YOu CLICK DA BUTTON WTPUAYCDB
#The FInal winnin window
def FC():
    FC = tk.Toplevel(root)
    FC.title("YOU DID IT")
    FC.geometry("400x400")
    label = tk.Label(FC, text="YOU HAVE WON THE GAME \n *TRUMPET SOUNDS BECASE WE CANT AFFORD TO HIRE REAL TRUMPET PLAYERS* \n *quiet sigh from the back of the audience* \n HOPE YOU ENJOYED ",
                     font=("Comfortaa", 32))

    FC.resizable(False, False)
    FC.attributes('-fullscreen', True)
    pygame.mixer.music.load("Sound/el-batido.mp3")  #Loads the sound onto the window
    pygame.mixer.music.play() #Plays the music when the player gets to the final window
    label.pack(padx=50,pady=100)
# {_  _}
# {0  0}
# { <  }
# { () }
    def close_FC(): #Closes Final Character Window
        FC.destroy()

        # CLOSE IT

    label.pack()  #Following code for the X out button
    exit_button = tk.Button(FC, text="X",
    command=close_FC,
    font=("Comfortaa", 30),
    bg="Red",
    fg="Black")
    exit_button.pack(pady=20)
    exit_button.place(x=1860, y=0)

    label.pack()
# {_  _}
# {X  X}
# { <  }
# {||| }
#You just made your final mistake

def FW(): #Making the Player think they have a limited amount of guesses
    FW = tk.Toplevel(root)
    FW.title("Demoralizing Info")
    y = root.winfo_y()
    x = root.winfo_x()
    FW.geometry("300x100+%d+%d" % (x + +200, y + 200))
    label = tk.Label(FW, text="You are getting scarily close to \n your final mistake XD XD XD")
    FW.resizable(False, False)
    label.pack()

    play_sound_effect(minion_sound) #Plays the Screaming Minion sound effect

    # Use tkinter's after method to call resume_music after the sound duration
    FW.after(int(minion_sound.get_length() * 1000), resume_music) #Resumes the backround music
#MERRY CHRISTMAS, WE ARE CHECKING FOR LOSSES MCWACFL
def CheckerC(Character): #Checks if the character the player clicked on is right or wrong
    if RandomCharacter == Character:
        FC() #Calls Final Character
    else:
        FW() #Calls Final Wrong

def CHAR(): #Character window
    CHAR = tk.Toplevel(root)
    CHAR.title("THE CHARACTERS")
    CHAR.geometry("400x400")
    label = tk.Label(CHAR, text="")
    CHAR.resizable(False, False)
    CHAR.attributes('-fullscreen',True)


#THIS IS WHERE WE CREATE THE BACKROUND COLOR For the Buttons
    def BGCOLOR():
        if RandomHouses == "Gryffindor":
            return "Red"
        elif RandomHouses == "Slytherin":
            return "Green"
        elif RandomHouses == "Ravenclaw":
            return "Blue"
        else: return "Yellow"

        # THIS IS WHERE WE CREATE THE FOREGROUND COLOR For the Buttons
    def FGCOLOR():
        if RandomHouses == "Gryffindor":
            return "White"
        elif RandomHouses == "Slytherin":
            return "White"
        elif RandomHouses == "Ravenclaw":
            return "White"
        else:
            return "Black"

    # THIS IS GONNA BE A FUNCTION THAT DOES WHAT? ITS GONNA PRINT OUT EACH CHARACTER AS A BUTTON DEPENDING ON THE RANDOM HOUSE SELECTED TIGBEFTDWIGPOECAABDOTRHS
    def BUTTONCREATOR(DAHOUSES,BGCOLOR,FGCOLOR):
        # Define starting coordinates for button placement
        x_start = 15  # Initial x-coordinate
        y_start = 79  # Initial y-coordinate
        x_offset = 403  # Horizontal spacing between buttons
        y_offset = 600  # Vertical spacing between buttons

        # Loop through the characters and create buttons
        for idx, DACHARACTERS in enumerate(DAHOUSES):
            row = idx // 5  # Calculate row number (3 buttons per row)
            col = idx % 5  # Calculate column number

            button = tk.Button(
                CHAR,
                text=DACHARACTERS,
                command=lambda DACHARACTERS=DACHARACTERS: CheckerC(DACHARACTERS),
                # Ensure the right character is passed
                font=("Comfortaa", 20),
                bg=BGCOLOR,
                fg=FGCOLOR,
                width=17,
                height=3,
            )
            button.pack(pady=5)

            # Use .place() for precise positioning
            button.place(x=x_start + col * x_offset, y=y_start + row * y_offset)
    # Define the main close function for CHAR
    def close_CHAR():
        CHAR.destroy()

    # CLOSE IT
    label.pack()
    exit_button = tk.Button(CHAR, text="X",
    command=close_CHAR,
    font=("Comfortaa", 30),
    bg="Red",
    fg="Black")
    exit_button.pack(pady=20)
    exit_button.place(x=1860, y=0)

    BUTTONCREATOR(YUMYUMYUMHOUSESTRING(RandomHouses),BGCOLOR(),FGCOLOR())


# WRONG ANWSER YOU NEED PSYCHIATRIC HELP
def Wrong():
    wrong = tk.Toplevel(root)
    wrong.title("Demoralizing Info")
    y = root.winfo_y()
    x = root.winfo_x()
    wrong.geometry("300x100+%d+%d" % (x + 200, y + 200))
    label = tk.Label(wrong, text="You Are Wrong \n Go Cry About it")
    wrong.resizable(False, False)

    play_sound_effect(minion_sound)

    # Use tkinter's after method to call resume_music after the sound duration
    #wrong.after(int(minion_sound.get_length() * 1000), resume_music)

    label.pack()




# CHECKER FOR WHETHER THEY SHOULD CRY OR NOT CFWTSCON

def Checker(House):
    if RandomHouses == House:
        CHAR()
    else:
        Wrong()
# Button that you click for TPAUG
Gbutton = tk.Button(root,
text="Gryffindor",
relief=tk.RAISED,
borderwidth=20,
command=lambda: Checker("Gryffindor"),
bg="red",
fg="white",
font=("bitter", 100))
Gbutton.pack(pady=10)
Gbutton.place(x=(WIDTH/2-850), y=(HEIGHT/2-400))
# THE EVIL BUTTON THAT NO ONE IS GONNA CLICK BUT THEN THEY GET JUMPSCARED
Sbutton = tk.Button(root,
text=" Slytherin ",
relief=tk.RAISED,
borderwidth=20,
command=lambda: Checker("Slytherin"),
bg="Green",
fg="white",
font=("bitter", 100))

Sbutton.pack(pady=10)
Sbutton.place(x=WIDTH/2+200, y=HEIGHT/2-400)
# HUFFLEPUFF BUTTON (NOT AN ENGLISH WORD) HBNAEW
Hbutton = tk.Button(root,
text="Hufflepuff ",
relief=tk.RAISED,
borderwidth=20,
command=lambda: Checker("Hufflepuff"),
bg="Yellow",
fg="Black",
font=("bitter", 100),)
Hbutton.pack(pady=10)
Hbutton.place(x=(WIDTH/2-860), y=(HEIGHT/2+100))  # Places Hbutton PHB

Rbutton = tk.Button(root,
text="Ravenclaw",
relief=tk.RAISED,
borderwidth=20,
command=lambda: Checker("Ravenclaw"),
bg="Blue",
fg="white",
font=("bitter", 100))
Rbutton.pack(pady=10)
Rbutton.place(x=WIDTH/2+200, y=HEIGHT/2+100)



root.mainloop()



















