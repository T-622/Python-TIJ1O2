# Done in VSCode & Python 3.8.4 32-bit
# Copyright 2020-2021 Tpeppy  
# Reproduction without citation is not permitted
# Licensed under GNU GPLv3.0 
# ANSI codes (\033[text style;text color;background color+m)
# TEXT STYLE CODE   TEXT COLOR	CODE   BACKGROUND COLOR	CODE
# No effect  0      Black	      30	   Black	            40
# Bold       1      Red	        31	   Red	              41
# Underline  2      Green	      32	   Green	            42
# Negative   3      Yellow	    33	   Yellow	            43
# Negative2  5      Blue	      34     Blue	              44
#                   Purple    	35	
#                   Cyan	      36	  
#                   White	      37	  
# Yellow = Prompt \033[1;33;40m
# Blue = Backstory \ Directions \033[1;36;40m
# Green = Accecpted \033[1;32;40m
# Red = Wrong / Error \ Death \033[1;31;40m
# Magenta = Info \033[1;35;40m
# The M charecter of the ANSI escape is squished with the first letter of the next sentance to avoid unneccesary spaces
# Closed 10/17/2020

stage = 1
health = 100 # Health variable as ongoing counter in the game.  We assign it 100 points to start.

import time  # Use time library for sleep function
import sys,os # Required for typewriter effect.

def typewriter (message): # VERY IMPORTANT: This is the typewriter effect used throghout the game. The waay it works is that we pass in our text and in exchange, the function prints that message with a predetemined pause in between each letter printing
  for char in message:
    sys.stdout.write (char)
    sys.stdout.flush()
    time.sleep(0.025)

def start_function():
    print("\033[1;35;40mQuick Note: If you die, the game ends and goes back to the main screen. Other instances like wrong input will send you back to the previous question.")
    print("\033[1;32;40m   _                                   _____  __   _   _                          ")              
    print("\033[1;32;40m  | |                                 |  _  |/ _| | | | |                         ")                
    print("\033[1;32;40m  | |     ___  __ _  __ _ _   _  ___  | | | | |_  | |_| | ___ _ __ ___   ___ ___  ") 
    print("\033[1;32;40m  | |    / _ \/ _` |/ _` | | | |/ _ \ | | | |  _| |  _  |/ _ | '__/ _ \ / _ / __| ")
    print("\033[1;32;40m  | |___|  __| (_| | (_| | |_| |  __/ \ \_/ | |   | | | |  __| | | (_) |  __\__ \ ")
    print("\033[1;32;40m  \_____/\___|\__,_|\__, |\__,_|\___|  \___/|_|   \_| |_/\___|_|  \___/ \___|___/ ")
    print("\033[1;32;40m                      _/ |                                                        ")  
    print("\033[1;32;40m                     |___/                                                        ") 
    print("")
    typewriter("\033[1;33;40mGood day hero, what be your name, brave one?: ")
    global name
    name = input()
    print("")
    time.sleep(1)
    typewriter("\033[1;36;40mHello %s, glad to have a protector for our kingdom!\n\n" % name)
    time.sleep(1)
    typewriter("\033[1;36;40mSo here's a bit of backstory %s. Recently, we have had many attacks on our kingdom by the almighty Icarus.\n" % name)
    typewriter("He has destroyed much of our teritory and has also taken the life of our most skilled and prized knight.\n")
    typewriter("Enough is enough! We need a brave knight like you %s, to protect our kingdom and restore our freedom!\n\n" % name)

def draw_castle(): # Castle ASCII art as function to make code tidier
    print("                           o                         ")
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

def draw_bridge():
 print("                                            ^^                        ")
 print("       ^^      ..                                       ..            ")
 print("             []                                       []              ")
 print("           .:[]:_          ^^                       ,:[]:.            ")
 print("         .: :[]: :-.                             ,-: :[]: :.          ")
 print("       .: : :[]: : :`._                       ,.': : :[]: : :.        ")
 print("     .: : : :[]: : : : :-._               _,-: : : : :[]: : : :.      ")
 print(" _..: : : : :[]: : : : : : :-._________.-: : : : : : :[]: : : : :-._  ")
 print(" _:_:_:_:_:_:[]:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:[]:_:_:_:_:_:_  ")
 print(" !!!!!!!!!!!![]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![]!!!!!!!!!!!!! ")
 print(" ^^^^^^^^^^^^[]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[]^^^^^^^^^^^^^ ")
 print("             []                                       []              ")
 print("             []                                       []              ")
 print("             []                                       []              ")
 print("  ~~^-~^_~^~/  \~^-~^~_~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/  \~^-~_~^-~~-  ")
 print(" ~ _~~- ~^-^~-^~~- ^~_^-^~~_ -~^_ -~_-~~^- _~~_~-^_ ~^-^~~-_^-~ ~^    ")
 print("    ~ ^- _~~_-  ~~ _ ~  ^~  - ~~^ _ -  ^~-  ~ _  ~~^  - ~_   - ~^_~   ")
 print("      ~-  ^_  ~^ -  ^~ _ - ~^~ _   _~^~-  _ ~~^ - _ ~ - _ ~~^ -       ")
 print("         ~^ -_ ~^^ -_ ~ _ - _ ~^~-  _~ -_   ~- _ ~^ _ -  ~ ^-         ")
 print("             ~^~ - _ ^ - ~~~ _ - _ ~-^ ~ __- ~_ - ~  ~^_-             ")
 print("                 ~ ~- ^~ -  ~^ -  ~ ^~ - ~~  ^~ - ~                   ")

def draw_end():
  print("  ________            ______          ____                                                     ")
  print(" /_  __/ /_  ___     / ____/___  ____/ / /                                                     ")
  print("  / / / __ \/ _ \   / __/ / __ \/ __  / /                                                      ")
  print(" / / / / / /  __/  / /___/ / / / /_/ /_/                                                       ")
  print("/_/_/_/_/_/\___/  /_____/_/_/_/\__,_(_)____                    __            _             __  ")
  print(" /_  __/ /_  ____ _____  / /_______   / __/___  _____   ____  / /___ ___  __(_)___  ____ _/ /  ")
  print("  / / / __ \/ __ `/ __ \/ //_/ ___/  / /_/ __ \/ ___/  / __ \/ / __ `/ / / / / __ \/ __ `/ /   ") 
  print(" / / / / / / /_/ / / / / ,< (__  )  / __/ /_/ / /     / /_/ / / /_/ / /_/ / / / / / /_/ /_/    ")
  print("/_/ /_/ /_/\__,_/_/ /_/_/|_/____/  /_/  \____/_/     / .___/_/\__,_/\__, /_/_/ /_/\__, (_)     ")
  print("                                                    /_/            /____/        /____/        ")


# Start of game
while True:
  start_function()
  while stage == 1: # Stage system that keeps you in the loop for stage 1 until the right path is chosen and stage is set to 2
    time.sleep(1)
    typewriter("\033[1;33;40mDo you accecpt this job? (y/n): ") # Prompt user for name input (used many times throughout the game)
    choice = input()
    if choice == "y": 
      typewriter("\033[1;36;40m\nGreat! Time to get you some armor.") # Pass in Ansi escape (\033) to change color
      time.sleep(1)
      typewriter("\033[1;36;40m\nSome time passes...")
      time.sleep(1)
      typewriter("\033[1;36;40m\nNow %s it is finally time for some action!"% name)
      time.sleep(1)
      typewriter("\033[1;36;40m\nAfter a long and treacherous journey by wagon, you finally arrive at almighty Icarus's castle. \nNow we need to find a way in. Any ideas? ")
      print("\n")
      time.sleep(2)
      draw_castle() 
      stage = 2 # Staging system. Set stage to next number when the correct answer is chosen. Also great opportunity for hidden stages
    elif choice == "n":
      typewriter("\033[1;31;40m\nGuess you can't handle this responsability. \nBye Bye!!")
      typewriter("\033[1;31;40m\nYou Died!")
      print("\033[0;30;40 ")
      break # Player died, throw them out and kill the program
    else:
      typewriter("\033[1;31;40mPlease try again and enter (y)es or (n)o\n") # As someone put in the wrong input, we print out a statement and then becuase stage is still stage = 1, the interpreter goes to while stage == 1 and repeats the loop until stage is set to another value.

  while stage == 2:
    print("")
    typewriter("\033[1;33;40mWhere shall we enter? (door, climb or run away): ")  
    enter = input ()
    print("")
    if enter == "door":
      typewriter("\033[1;36;40mWise choice to go for the obvious (not)")
      typewriter("\033[1;36;40m\nUpon entering, you see this: ")
      print("")
      time.sleep(1)
      draw_dog()
      time.sleep(1.5)
      typewriter("\033[1;31;40mIn panic, you soil yourself and the dog eats you for an appetizer. Better luck next time!")
      break
      
    elif enter =="run away" :
      typewriter("\033[1;31;40mWow, great hero choice.\n")
      
    elif enter == "climb" :
      typewriter("\033[1;32;40mFinally, some sense!")
      time.sleep(1.5)
      typewriter("\033[1;36;40m\nYou take some small fall damage from the jump into the castle but, nothing much.")
      time.sleep(1)
      health = health - 20
      typewriter("\033[1;35;40m\nHP=%s" % health)
      typewriter("\033[1;36;40m\nYou are now over the wall and in a corridor of sorts.")
      typewriter("\033[1;36;40m\nAfter dusting yourself off %s you disover that there are guards watching you." % name)
      print("")
      stage = 3
    else: 
      typewriter("\033[1;31;40mPlease input where you would like to enter (door, climb or run away)")
      time.sleep(1)

  while stage == 3:    
    typewriter("\033[1;33;40m\nHow do you handle this situation? (fight, i want my mommy, hide): ")
    guards = input ()
    print("")
    if guards == "fight":
      time.sleep(1)
      typewriter("\033[1;31;40mNormally a great idea, but you only realise that you don't have weapons.\n")
      typewriter("\033[1;31;40mYou Died!")
      break
    elif guards == "i want my mommy":
      time.sleep(1)
      typewriter("\033[1;31;40mWhy did we choose you as a knight?? Let's try this again.\n")
    elif guards == "hide":
      time.sleep(1)
      typewriter("\033[1;32;40mWell, what a smart cookie! The guards are so dumb that they don't notice you and walk past you.")
      typewriter("\033[1;36;40m\nAfter waiting a small bit, you finally get an opportunity to get away...\n") 
      time.sleep(1)
      typewriter("\033[1;36;40m\nYou enter the hallway only to be met by a TRAP!")
      typewriter("\033[1;36;40m\nBecause this castle has some upgrades, we need to solve an equation in order to get a code\n")
      stage = 4
    else:
      typewriter("\033[1;31;40mI don't understand\n")
      
  while stage == 4:
    trap = input("\033[1;33;40m\nPlease enter the code (12*2 divided by 6): ")
    if (trap.isnumeric() and trap == "4") :
      typewriter("\033[1;32;40m\nAccess granted, you must now cross the rickety bridge.")
      time.sleep(1)
      draw_bridge()
      typewriter("\033[1;36;40m\nYou nervously cross the long bridge unknowing what fate lies ahead...")
      time.sleep(1)
      typewriter("\033[1;36;40m\nWhen you finish crossing the bridge, a mysterious and thick fog magically appears...")
      time.sleep(1)
      typewriter("\033[1;36;40m\nYou now see you have 2 options, go to a room full of treasure or, continue on your path to fight Icarus")
      print("")
      stage = 5
    else:  # Try to invalidate wrong / non-integer input 
      typewriter("\033[1;31;40m\nWrong code, please enter a number.")

  while stage == 5: 
    print("")  
    typewriter("\033[1;33;40mWhich way will it be? (gimme da gold, i'm smarter than that): ")
    path = input ()
    print()
    if path == "gimme da gold":
      typewriter("\033[1;36;40mYou take a step inside and feast your eyes on gold! Mounds of it!")
      time.sleep(2)
      typewriter("\033[1;36;40m\nAfter eternities of basking in gold, you decide to head home with a souvenir. \nLittle did you know your so called souvenir turned out to be an alarm lever.\nThe guards are informed and you are placed in a battle. You eventually fight them off, but this results in a weak hero. ")
      health = health - 30
      typewriter("\033[1;35;40m\nHP=%s"% health)
      stage = "5a"
      
    elif path == "i'm smarter than that":
      typewriter("\033[1;32;40mI guess you really are then!")
      time.sleep(1)
      typewriter("\033[1;36;40m\nWe are now at one of the final stages. Buckle up,")
      time.sleep(1)
      print("\n")
      stage = 6
    else:
      typewriter("\033[1;31;40mNice try smart one!")

  while stage == "5a": # Hidden stage
    print()  
    typewriter("\033[1;33;40m\n2 routes out of here, an unmarked door or the path back onto your journey (door, continue): ")
    specialstage = input ()
    print()
    if specialstage == "door":
      typewriter("\033[1;36;40mYou take a step inside and find an eerie blue glowing substance. You taste it.")
      time.sleep(2)
      typewriter("\033[1;36;40m\nFortunately, this was a secret healing potion. You now gain +20 HP.")
      health = health + 20
      typewriter("\033[1;35;40m\nHP=%s"% health)
      typewriter("\033[1;36;40m\nYou also get transported back onto the intended path.")
      stage = 6
      
    elif specialstage == "continue":
      time.sleep(2)
      stage = 6
    else:
      typewriter("\033[1;31;40mReally thought you could actually fool me?")
  
  while stage == 6:
    typewriter("\033[1;36;40m\nYou have 2 final objects in the way though that you need to cross, one is a lava moat with stones that move. \nThe second is a drawbridge door you need to unjam.")
    time.sleep(1)
    typewriter("\033[1;36;40m\nNow our little hot lava problem. \nWe have 3 ways to get across, we jump, we think strategically or we give up\n")
    typewriter("\033[1;33;40m\nWhat will it be? (jump, think, give up): ")
    lavaquestion = input ()
    if lavaquestion == "jump":
      typewriter("\033[1;31;40mEver heard of slipping? Yea, you kinda did...")
      typewriter("\033[1;31;40m\nYou Died!")
      break
    elif lavaquestion == "give up":
      typewriter("\033[1;31;40mHoly cow, we need to have a chat with the people that pick these warriors!")
    elif lavaquestion =="think":
      typewriter("\033[1;32;40mAlright! You got it right!")
      time.sleep(1)
      typewriter("\033[1;36;40m\nLast obstacle!")
      time.sleep(1)
      typewriter("\033[1;36;40m\nIn order to unjam this moat gearing system, we must remove the blockade and lower the door quietly to avoid people noticing!")
      time.sleep(1)
      typewriter("\033[1;36;40m\n2 Ways of doing this. 1 is that we use brute force and 2 is that we lower the gate and hope the weight of the door crushes the blockade\n")
      time.sleep(1)
      stage = 7
    else:
      typewriter("\033[1;31;40mThink you're funny?\n")
      

  while stage == 7:    
    print("")
    typewriter("\033[1;33;40mC'mon, last time, what will it be? (brute, brains): ")
    lastquestion = input ()
    print()
    if lastquestion == "brute":
      typewriter("\033[1;36;40mWe manage to open the door and remove our blockade, but, upon lowering the door, you realise beans for breakfast wasn't the best idea.")
      time.sleep(1)
      typewriter("\033[1;36;40m\nA green cloud appears and noise is emitted at record breaking levels!")
      time.sleep(1)
      typewriter("\033[1;31;40m\nGreat going farting %s"% name)
      time.sleep(1)
      typewriter("\033[1;31;40m\nYou Died!\n")
      break
    elif lastquestion == "brains":
      typewriter("\033[1;32;40mGreat choice %s Thanks to that, we now got into the building unnoticed." % name)
      time.sleep(1)
      typewriter("\033[1;36;40m\nNow, we stand in front of the almighty Icarus. A colourful conversation goes something like this.")
      time.sleep(1)
      typewriter("\033[1;36;40m\nIcarus: What are you doing here %s ?"% name)
      time.sleep(1)
      typewriter("\033[1;36;40m\n%s: I have been summoned to settle the battle and throw down some beef (ง •̀_•́)ง  ლ( `Д’ ლ)" % name)
      time.sleep(1)
      typewriter("\033[1;36;40m\nIcarus: No")
      time.sleep(1)
      typewriter("\033[1;36;40m\n%s: Yes"% name)
      time.sleep(1)
      typewriter("\033[1;36;40m\nIcarus: No. I say no and what I say goes around here.")
      time.sleep(1)
      typewriter("\033[1;36;40m\nIcarus gets up on his feet and decides to battle it out.\nYou two decide to settle this never ending battle.")
      time.sleep(1)
      typewriter("\033[1;36;40m\n%s Listen up. this will be a make or break decision that succedes or flops.\n"% name)
      
      stage = 8
    else: 
      typewriter("\033[1;31;40mChoose a real option")

  while stage == 8:
    print("")
    typewriter("\033[1;33;40mWhat will it be? (suprise attack, invisible potion, sit and hope) : ")
    bossbattle = input ()
    
    if bossbattle == "suprise attack":
      typewriter("\033[1;31;40mYou see, suprise attacking a 7'7 man is not really a great idea.")
      typewriter("\033[1;31;40m\nYou Died!")
      break
    elif bossbattle == "invisible potion":
      typewriter("\033[1;32;40m\nGreat thought!")
      time.sleep(1)
      typewriter("\033[1;36;40m\nYou pull a bottle of liquid from your pocket.")
      time.sleep(1)
      typewriter("\033[1;36;40m\nYou down it. Dammit... that was the 7up.")
      time.sleep(1)
      typewriter("\033[1;36;40m\nYou grab another bottle, this time labeled invisi-potion.")
      time.sleep(1)
      typewriter("\033[1;36;40m\nYou down it so fast, they couldn't see you do it! (No pun intended).")
      time.sleep(1)
      typewriter("\033[1;36;40m\nYou make a superb shot to the jugular which kills Icarus entirely.\n") # Remember to add great outro to the game 
      stage = "END"
    elif bossbattle == "sit and hope":
      typewriter("\033[1;31;40mIcarus eats you for a snack. You die concequently")
      typewriter("\033[1;31;40mYou Died!\n")
      break
    else:
      typewriter("\033[1;31;40mChoose a real option")
  
  while stage == "END":
    print("")
    typewriter("\033[1;36;40mThe aftermath was amazing. People from all around gathered outside the castle applauding becuase of the defeat.")
    time.sleep(1)
    typewriter("\033[1;36;40m\nUpon returning to the village, you are greeted by your king. He now presentes you with the medal of service.")
    time.sleep(1)
    typewriter("\033[1;36;40m\nGreat job %s all are very proud and safe to have a protector like you!\n"% name)
    time.sleep(1)
    draw_end()
    typewriter("\033[1;32;40m\nCheck me out and find the source code on GitHub https://github.com/T-622/Python-TIJ1O2")     
    time.sleep(1)
    stage = 10 #there is no stage 10 so this causes the loop to end rather than the break under it which causes it to stop after stage 9 is done (basically repeating stage 9 forever becuase it is always set to stage = 9)
  break


         

    

   
      