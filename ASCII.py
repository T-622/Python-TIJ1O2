def start_function():
    print("    _                                   _____  __   _   _                          ")                       
    print("   | |                                 |  _  |/ _| | | | |                         ")                       
    print("   | |     ___  __ _  __ _ _   _  ___  | | | | |_  | |_| | ___ _ __ ___   ___ ___  ") 
    print("   | |    / _ \/ _` |/ _` | | | |/ _ \ | | | |  _| |  _  |/ _ | '__/ _ \ / _ / __| ")
    print("   | |___|  __| (_| | (_| | |_| |  __/ \ \_/ | |   | | | |  __| | | (_) |  __\__ \ ")
    print("   \_____/\___|\__,_|\__, |\__,_|\___|  \___/|_|   \_| |_/\___|_|  \___/ \___|___/ ")
    print("                       _/ |                                                        ")  
    print("                      |___/                                                        ") 
    name = input("Good day hero, what shall we call you?: ") 
    print("Hello",name,",glad to have a protector for our kingdom")
    print()
    print("So here's a bit of backstory",name,", recently, we have had may attacks on our kingdom from the almighty Icarus. \n He has destroyed very much of our teritory, urnfortunately, he also took the life of our most skilled and prized night. \n Enough is enough. We need a brave night like you",name,"to protect our kingdom and restore our freedom.")
    
while True:
    start_function()
    Join = input("Do you accecpt this job? (y/n): ")
    if Join == "y":
        print("Great! time to get you some armor")
        
        break
    elif Join == "n" :
        print("Guess you can't handle this responability. \n Bye Bye")
        print("You Died")
        break