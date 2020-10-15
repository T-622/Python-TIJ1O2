# Copyright 2020-2021 Tpeppy  
# Reproduction without citation is not permitted
# Licensed under GNU GPLv3.0 
# ANSI codes (\033[text style;text color;background color)
# TEXT COLOR	CODE	TEXT STYLE	CODE	BACKGROUND COLOR	CODE
# Black	        30	    No effect	0	    Black	            40
# Red	        31	    Bold	    1	    Red	                41
# Green	        32	    Underline	2	    Green	            42
# Yellow	    33	    Negative1	3	    Yellow	            43
# Blue	        34   	Negative2	5	    Blue	            44
# Purple    	35		Purple	    45
# Cyan	        36		Cyan	    46
# White	        37		White	    47


health = 100 # Health variable as ongoing counter in the game
import time  # Use time library for sleep function
def start_function():
    print("\033[1;32;40m    _                                   _____  __   _   _                          ")                       
    print("\033[1;32;40m   | |                                 |  _  |/ _| | | | |                         ")                       
    print("\033[1;32;40m   | |     ___  __ _  __ _ _   _  ___  | | | | |_  | |_| | ___ _ __ ___   ___ ___  ") 
    print("\033[1;32;40m   | |    / _ \/ _` |/ _` | | | |/ _ \ | | | |  _| |  _  |/ _ | '__/ _ \ / _ / __| ")
    print("\033[1;32;40m   | |___|  __| (_| | (_| | |_| |  __/ \ \_/ | |   | | | |  __| | | (_) |  __\__ \ ")
    print("\033[1;32;40m   \_____/\___|\__,_|\__, |\__,_|\___|  \___/|_|   \_| |_/\___|_|  \___/ \___|___/ ")
    print("\033[1;32;40m                       _/ |                                                        ")  
    print("\033[1;32;40m                      |___/                                                        ") 
    global name # Allow name to be used globally not locally
    name = input("\033[1;36;40m Good day hero, what shall we call you?: ") 
    time.sleep(1)
    print("Hello",name,",glad to have a protector for our kingdom")
    print()
    time.sleep(2)
    print("\033[1;34;40m So here's a bit of backstory",name,"recently, we have had may attacks on our kingdom from the almighty Icarus. \n He has destroyed very much of our teritory, unfortunately, he also took the life of our most skilled and prized knight. \n Enough is enough. We need a brave knight like you",name,"to protect our kingdom and restore our freedom.")
    
def draw_castle(): # Castle ASCII art as function to make code tidier
    print("                          o                          ")
    print("                       _---|         _ _ _ _ _       ")
    print("                    o   ---|     o   ]-I-I-I-[       ")
    print("   _ _ _ _ _ _  _---|      | _---|    \ ` ' /        ")
    print("   ]-I-I-I-I-[   ---|      |  ---|    |.   |         ")
    print("    \ `   '_/       |     / \    |    | /^\|         ")
    print("     [*]  __|       ^    / ^ \   ^    | |*||         ")
    print("     |__   ,|      / \  /    `\ / \   | ===|         ")
    print("  ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|         ")
    print("  I_I__I_I__I_I  (====(_________)___|_|____|____     ")
    print("  \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_|     ")
    print("   |[]      '|   | []  |`__  . [  \-\--|-|--/-/      ")
    print("   |.   | |' |___|_____I___|___I___|---------|       ")
    print("  / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] |       ")
    print(" <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \      ") 
    print(" ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===>     ")
    print(" ] []| ` |   ||||||||||||||||||||.||__.  | |[] [     ") 
    print(" <===>     ' ||||| |   |   | ||||.||  []   <===>     ")
    print("  \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/      ")
    print("   |      . _||||| |   |   | ||||.|| |     | |       ")
    print("../|' v . | .|||||/____|____\|||| /|. . | . ./       ")
    print(".|//\............/...........\........../..////      ") 

def draw_dog(): # Dog ASCII art
    print("                                         /\ /\                ")
    print("                                        /  \---._             ")  
    print("                                         / / `     `\         ")      
    print("                                         \ \   `'<@)@)        ")
    print("                                         /`         ~ ~._     ")
    print("                                        /                `()  ")
    print("                                       /    \   (` ,_.:.  /   ")
    print("                                      / ~    `\   (vVvvvvV    ")
    print("                                     /       |`\_ `^^^/       ")
    print("                                 ___/________|_  `---'        ")
    print("                                (_____R_E_X____) _            ")
    print("                                _/~          | `(_)           ")
    print("                              _/~             \               ")
    print("                            _/~               |               ")
    print("                          _/~                 |               ")
    print("                        _/~                   |               ")
    print("                      _/~         ~.          |               ")
    print("                    _/~             \        /\               ")
    print("                 __/~               /`\     `||               ")
    print("               _/~      ~~-._     /~   \     ||               ")
    print("              /~             ~./~'      \    |)               ")
    print("             /                 ~.        \   )|               ")
    print("            /                    :       |   ||               ")
    print("    Tpeppy  |                    :       |   ||               ")
    print("            |                   .'       |   ||               ")
    print("       __.-`                __.'--.      |   |`---.           ")
    print("    .-~  ___.         __.--~`--.))))     |   `---.)))         ")
    print("   `---~~     `-...--.________)))))      \_____)))))          ")

# Start of game

while True:
    start_function()
    Join = input("Do you accecpt this job? (y/n): ")
    if Join == "y":
        print("\033[1;37;40m Great! time to get you some armor") # Pass in Ansi escape (\033) to change color
        time.sleep(1)
        print("Some time passes...")
        print("Now",name,"it is finally time for some action!")
        time.sleep(1)
        print("\033[2;37;40m Ater a long and treacherous journey by wagon, you finally arrive at almighty Icarus's castle. \n Now we need to find a way in. Any ideas? ")
        time.sleep(3)
        draw_castle() 
        enter = input("Where shall we enter? (enter: door, climb or run away): ")
        if enter == "door" :
          print("Wise choice to go for the obvious (not)")
          print("Upon entering, you see this: ")
          time.sleep(2)
          draw_dog()
          time.sleep(1.5)
          print("\033[1;31;40m In panic, you soil yourself and the dog eats you for an appetiser. Better luck next time")
          break

        elif enter =="run away" :
         print("\033[1;31;40m Wow, great hero choice.")
         break

        elif enter == "climb" :
         print("\033[1;32;40m Finally, some sense!")
         print("You take some small fall damage from the jump but, nothing much")
         print("\033[1;31;40m HP: ")
         print(health = health - 10)

        else : 
         print("\033[2;31;40m Please input where you would like to enter properly")
         time.sleep(1)

    elif Join == "n" :
        print("Guess you can't handle this responability. \n Bye Bye")
        print("\033[0;37;41m You Died")
        break

    else:
     print("\033[1;31;40m Please try again and enter y or n (no caps) for Yes or No")
      