#April 1, 2024
#Major poject - Samarveer Shergill
#Haunted Mansion - Escape mission

#Welcome to "The Haunted Mansion Escape Mission"
#a spine-chilling text-based RPG where you explore the eerie depths of an ancient, haunted mansion.
#Unravel dark secrets, encounter restless spirits and creatures, and survive the night if you dare.
#Your adventure begins now!

    
import time                                                               #imports 'time' 

def print_with_delay(text, delay):                                        #defines the function print_with_delay
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()                                                               # Print a newline after the text is fully printed

def play_again():                                                         #defines the function play_again
    decision = input("Would you like to play again? (yes/no): ")          #asks for user input
    if decision.lower() == "yes":                                         #conditional statement
        start_game()                                                      #starts the game again
        
    elif decision.lower() == "no":                                        #conditional statement
        print_with_delay("Thanks for playing! Goodbye.", 0.05)
    else:                                                                 #conditional statement
        print_with_delay("Invalid choice. Please enter 'yes' or 'no'.", 0.05)

def start_game():                                                                                     #defines the function start_game
    print_with_delay("Welcome to the Haunted Mansion Escape Mission!", 0.05)
    print_with_delay("You find yourself in front of a dimly lit, eerie mansion.", 0.05)
    decision = input("Would you like to investigate the mansion or leave? (investigate/leave): ")      #asks for user input
    if decision.lower() == "investigate":                                                              #conditional statement
        event2()                                                                                       #calls event2()
    elif decision.lower() == "leave":                                                                  #conditional statement
        play_again()                                                                                   #calls the function play_again()                 
    else:                                                                                              #conditional statement
        print_with_delay("Invalid choice. Please enter 'investigate' or 'leave'.", 0.05)
        start_game()                                                                                   #calls the function start_game()
def event2():                                                                                          #defines event2()
    print_with_delay("As you explore, you encounter a ghost!", 0.05)
    decision = input("Would you like to communicate with the ghost or run away? (communicate/run away): ")  #asks for user input
    if decision.lower() == "communicate":                                                                   #conditional statement
        communicate_with_ghost()                                                                            #calls communicate_with_ghost()
    elif decision.lower() == "run away":                                                                    #conditional statement
        print_with_delay("You run away and find yourself in a dark empty corridor with a room at the end.", 0.05)
        event3()                                                                                            #goes to event3()
    else:                                                                                                   #conditional statement
        print_with_delay("Invalid choice. Please enter 'communicate' or 'run away'.", 0.05)
        event2()                                                                                            #calls event2()

def communicate_with_ghost():                                                                               #defines communicate_with_ghost()                                   
    print_with_delay("The ghost gives you a clue:", 0.05)
    print_with_delay("According to the ghost, you are stuck in a haunted mansion full of booby traps and dangerous creatures.", 0.05)
    print_with_delay("The only way to escape is by finding a magical key hidden somewhere in the mansion.", 0.05)
    print_with_delay("Use the key to unlock the door you entered from.", 0.05)
    print_with_delay("Now, you must decide whether to continue exploring or leave the mansion.", 0.05)
    decision = input("Would you like to continue exploring or leave? (explore/leave): ")                      #asks for user input
    if decision.lower() == "explore":                                                                         #conditional statement
        print_with_delay("You continue your exploration.", 0.05)
        print_with_delay("After a while, you find an open door.", 0.05)
        event4()                                                                                              #calls event4()
    elif decision.lower() == "leave":                                                                         #conditional statement
        print_with_delay("Back to Start.", 0.05)
        play_again()                                                                                          #calls play again()

    else:                                                                                                     #conditional statement
        print_with_delay("Invalid choice. Please enter 'explore' or 'leave'.", 0.05)
        communicate_with_ghost()                                                                               #calls commnuicate with ghost()   
        
def event3():                                                                                                  #defines event3()
    print_with_delay("The corrdior turns right and there is a room in front of you .", 0.05)
    decision = input("Would you like to keep running or enter the room? (run/enter): ")                        #asks for user input
    if decision.lower() == "enter":                                                                            #conditional statement
        print_with_delay("You enter a room and find yourself in a mirror maze.", 0.05)
        print_with_delay("You try to find your way out but get trapped.", 0.05)
        print_with_delay("Unfortunately, you starve and perish in the maze.", 0.05)
        print_with_delay("Game Over!", 0.05)
        play_again()                                                                                            #calls play_again()
    elif decision.lower() == "run":                                                                             #conditional statement
        print_with_delay("You choose to run forward.", 0.05)
        print_with_delay("You encounter giant spiders!", 0.05)
        print_with_delay("You try to make a run for it but the spiders catch up to you.", 0.05)
        print_with_delay("You die. Game Over!", 0.05)
        play_again()                                                                                            #calls play_again()
    else:                                                                                                       #conditional statement
        print_with_delay("Invalid choice. Please enter 'run' or 'enter'.", 0.05)
        event3()                                                                                                #calls event3()
        
def event4():                                                                                                   #defines event4()
    print_with_delay("You find an open door.", 0.05)
    decision = input("Would you like to investigate the room or keep moving forward? (investigate/keep moving): ")    #asks for user input
    if decision.lower() == "investigate":                                                                             #conditional statement
        print_with_delay("You step in the door and a giant axe comes flying towards you.", 0.05)
        print_with_delay("You die. Game Over!", 0.05)
        play_again()                                                                                                  #calls play_again()
    elif decision.lower() == "keep moving":                                                                           #conditional statement
        print_with_delay("You decide to keep moving forward.", 0.05)
        print_with_delay("You find a wall with a riddle written on it.", 0.05)
        search_riddle()                                                                                               #calls search_riddle()
    else:                                                                                                             #conditional statement
        print_with_delay("Invalid choice. Please enter 'investigate' or 'keep moving'.", 0.05)
        event4()                                                                                                      #calls event4()

def search_riddle():                                                                                                  #defines search_riddle()
    print_with_delay("After finding the riddle, you have two choices:", 0.05)
    decision = input("Would you like to search for clues in the riddle or keep moving forward? (search/keep moving): ")   #asks for user input
    if decision.lower() == "search":                                                                                      #conditional statement                                        
        print_with_delay("You try to find clues in the riddle but can't find any.", 0.05)
        print_with_delay("You must make another decision.", 0.05)
        another_decision()                                                                                                #calls another_decision()
    elif decision.lower() == "keep moving":                                                                               #conditional statement
                print_with_delay("You decide to keep moving forward.", 0.05)
                print_with_delay("You see hundreds of bats flying towards you.", 0.05)
                print_with_delay("you make a run for it!", 0.05)
                event5()                                                                                                  #calls event5()
    else:                                                                                                                 #conditional statement
        print_with_delay("Invalid choice. Please enter 'search' or 'give upkeep moving'.", 0.05)
        search_riddle()                                                                                                #calls search_riddle()
        
def another_decision():                                                                                                #defines another_decision
    decision = input("Would you like to keep moving forward or give up? (keep moving/give up): ")                      #asks for user input
    if decision.lower() == "keep moving":                                                                              #conditional statement
                print_with_delay("You decide to keep moving forward.", 0.05)
                print_with_delay("You see hundreds of bats flying towards you.", 0.05)
                print_with_delay("you make a run for it!", 0.05)
                event5()                                                                                               #calls event5()
    elif decision.lower() == "give up":                                                                                #conditional statement
        print_with_delay("You give up.", 0.05)
        print_with_delay("You starve and eventually die.", 0.05)
        print_with_delay("Game Over!", 0.05)
        play_again()                                                                                                   #calls play_again()
    else:                                                                                                              #conditional statement
        print_with_delay("Invalid choice. Please enter 'keep moving' or 'give up'.", 0.05)
        search_riddle()                                                                                                 #calls search_riddle()
        
def event5():                                                                                                           #defines event5()
    print_with_delay("You are being chased by hundreds of bats and are running for your life.", 0.05)
    decision = input("There's a room close by. Would you like to keep running or get in the room? (keep running/get in the room): ")   #asks for user input
    if decision.lower() == "keep running":                                                                                 #conditional statement
        print_with_delay("You decide to keep running.", 0.05)
        print_with_delay("You keep running to find the entrance you came in from but you're lost in the maze of corridors.", 0.05)
        print_with_delay("The bats eventually catch up to you. You die. Game Over!", 0.05)
        play_again()                                                                                                       #calls play_again()
    elif decision.lower() == "get in the room":                                                                            #conditional statement
        print_with_delay("You decide to get in the room.", 0.05)
        print_with_delay("The room looks awfully suspicious, with a big painting on the wall and books lying all around on the floor.", 0.05)
        search_room()                                                                                                      #calls search_room()
    else:                                                                                                                  #conditional statement
        print_with_delay("Invalid choice. Please enter 'keep running' or 'get in the room'.", 0.05)
        event5()                                                                                                            #calls event5()

def search_room():                                                                                                          #defines search_room()
    print_with_delay("You search for clues in the room and find out that the eyes on the painting are actually switch buttons to something unknown.", 0.05)
    print_with_delay("You must make a decision.", 0.05)
    decision = input("Would you like to press the switch buttons or leave the room? (press buttons/leave): ")                #asks for user input
    if decision.lower() == "press buttons":                                                                                  #conditional statement
        print_with_delay("You press the switch buttons on the painting.", 0.05)
        print_with_delay("The painting turns around 180*.", 0.05)
        print_with_delay("The back of the painting has a metal door with a warning sign and a code written on it.", 0.05)
        event6()                                                                                                             #calls event6()
        
    elif decision.lower() == "leave":                                                                                        #conditional statement
        print_with_delay("You decide to leave the room and continue your escape.", 0.05)
        print_with_delay("You encounter more bats in the corridor", 0.05)
        print_with_delay("Bats chase you and catch up to you, unfortunately you die", 0.05)
        play_again()                                                                                                         #calls play_again()
        

    else:                                                                                                                    #conditional statement
        print_with_delay("Invalid choice. Please enter 'press buttons' or 'leave'.", 0.05)
        search_room()                                                                                                        #calls search_room()
        
        
def event6():                                                                                                                  #defines event6()
    decision = input("What will you do? Give up and hope help arrives or enter the code to the door? (give up/enter code): ")  #asks for user input
    if decision.lower() == "give up":                                                                                          #conditional statement
        print_with_delay("You decide to give up.", 0.05)
        print_with_delay("Unfortunately, help does not arrive, and you starve.", 0.05)
        print_with_delay("Eventually you die. Game Over!", 0.05)
        play_again()                                                                                                            #calls play_again()
    elif decision.lower() == "enter code":                                                                                      #conditional statement
        print_with_delay("You enter the code to the vault.", 0.05)
        enter_code_to_vault()                                                                                                   #calls enter_code_to_vault()     
    else:                                                                                                                       #conditional statement
        print_with_delay("Invalid choice. Please enter 'give up' or 'enter code'.", 0.05)
        event6()                                                                                                                 #calls event6()

def enter_code_to_vault():                                                                                                       #defines enter_code_to_vault()  
    print_with_delay("The door screeches and slowly opens revealin a hidden passage!", 0.05)
    decision = input("Do you want to go inside down the hidden passage or go outside to keep going deeper into the mansion to find an alternate exit (inside the passage/try to find and alternate exit): ")   #asks for user input
    if decision.lower() == "inside the passage":                                                                                  #conditional statement
        event7()                                                                                                                  #calls event7()
        
    elif decision.lower() == "try to find and alternate exit":                                                                    #conditional statement                                                              
        print_with_delay("You decide not to enter the door and explore deeper into the mansion.", 0.05)
        print_with_delay("You go outside but are stuck in the maze of corridors and encounter more deadly creatures, unfortunately, you perish.", 0.05)
        print_with_delay("Game Over!", 0.05)
        play_again()                                                                                                               #calls play_again()
    else:                                                                                                                          #conditional statement
        print_with_delay("Invalid choice. Please enter 'inside the passage' or 'try to find and alternate exit'.", 0.05)
        enter_code_to_vault()                                                                                                       #calls enter_code_to_vault()  

def event7():                                                                                                                       #defines event7()
    print_with_delay("As you continue deeper into the hidden passage, you hear faint whispers and eerie sounds.", 0.05)
    decision = input("Do you investigate the source of the sounds or go back? (investigate/go back): ")                             #asks for user input
    if decision.lower() == "investigate":                                                                                           #conditional statement
        print_with_delay("You follow the sounds and discover a hidden room with ancient artifacts.", 0.05)
        print_with_delay("Step by step you keep moving forward and go into a hidden compartment that leads to another passage going deep inside the building.", 0.05)
        event8()                                                                                                                     #calls event8()
        
    elif decision.lower() == "go back":                                                                                              #conditional statement
        print_with_delay("You proceed back cautiously, avoiding the unknown sounds.", 0.05)
        print_with_delay("You're back in the room and close the metal door.", 0.05)
        print_with_delay("You try to find more clues in the room.", 0.05)
        print_with_delay("Unfortunately you cant find anymore clues, you starve and you perish.", 0.05)
        print_with_delay("Game Over!", 0.05)
        play_again()                                                                                                                 #calls play_again()

    else:                                                                                                                            #conditional statement
        print_with_delay("Invalid choice. Please enter 'investigate' or 'go back'.", 0.05)
        event7()                                                                                                                     #calls event7()


def event8():                                                                                                                        #defines event8()
    print_with_delay("Eventually, You reach a grand hall with multiple doors leading to different directions.", 0.05)
    print_with_delay("Now you have to make a decision based truly on your gut !!", 0.05)
    decision = input("Which door do you choose? Left, Right, or Straight? (left/right/straight): ")                                 #asks for user input
    if decision.lower() == "left":                                                                                                  #conditional statement
        print_with_delay("You enter the left door and find yourself in a dark library filled with ancient books.", 0.05)
        print_with_delay("One book stands out—it seems to have a lock on its front case and you can't open it without its key.", 0.05)
        decision = input("Do you investigate and try to pick the lock or continue exploring the library? (pick lock/continue exploring): ")    #asks for user input
        if decision.lower() == "pick lock":                                                                                                    #conditional statement
            print_with_delay("You attempt to pick the lock but trigger a trap, releasing poisonous gas.", 0.05)
            print_with_delay("You narrowly escape the gas but are weakened.", 0.05)
            print_with_delay("You feel your heartbeat getting faster.", 0.05)
            print_with_delay("Your hands and feet are getting cold", 0.05)
            print_with_delay("Looks like the poison has taken a toll on you", 0.05)
            print_with_delay("You fall down, you die", 0.05)
            print_with_delay("Game over!", 0.05)
            play_again()                                                                                                              #calls play_again()
        elif decision.lower() == "continue exploring":                                                                                #conditional statement
            print_with_delay("You decide to continue exploring the library.", 0.05)
            event9()                                                                                                                   #calls event9()
        else:                                                                                                                          #conditional statement
            print_with_delay("Invalid choice. Please enter 'pick lock' or 'continue exploring'.", 0.05)
            event8()                                                                                                                    #calls event8()
    elif decision.lower() == "right":                                                                                                   #conditional statement
        print_with_delay("You enter the right door and find a dining hall with a lavish feast set out.", 0.05)
        print_with_delay("However, the food looks suspiciously untouched.", 0.05)
        decision = input("Do you eat the food or search for clues? (eat/search): ")                                                   #asks for user input
        if decision.lower() == "eat":                                                                                                 #conditional statement
            print_with_delay("You eat the food and feel a strange sensation, weakening your senses.", 0.05)
            print_with_delay("OH NO! The food was poisoned, You Die.", 0.05)
            print_with_delay("Game Over!", 0.05)
            play_again()                                                                                                              #calls play_again()
        elif decision.lower() == "search":                                                                                            #conditional statement
            print_with_delay("You search the dining hall and find hidden messages under the plates.", 0.05)
            print_with_delay("The message says ", 0.05)
            print_with_delay("YOU CHOSE THE WRONG DOOR!", 0.05)
            print_with_delay("A Giant Axe comes flying towrads you", 0.05)
            print_with_delay("You die", 0.05)
            print_with_delay("Game over", 0.05)
            play_again()                                                                                                               #calls play_again()
        else:                                                                                                                          #conditional statement
            print_with_delay("Invalid choice. Please enter 'eat' or 'search'.", 0.05)
            event8()                                                                                                                   #calls event8()
    elif decision.lower() == "straight":                                                                                               #conditional statement
        print_with_delay("You choose the straight door and as soon as you enter the room the door closes behind you.", 0.05)
        print_with_delay("all of a sudden there is a massive fire in the room.", 0.05)
        print_with_delay("You Perish.", 0.05)
        print_with_delay("Game Over!", 0.05)
        play_again()                                                                                                                     #calls play_again()
        
    else:                                                                                                                                #conditional statement
        print_with_delay("Invalid choice. Please enter 'left', 'right', or 'straight'.", 0.05)
        event8()                                                                                                                         #calls event8()

def event9():                                                                                                                            #defines event9()
    print_with_delay("You see various abandoned books and spooky objects as you explore the library.", 0.05)
    print_with_delay("You accidentally step on a button, and one of the library shelves opens up to reveal another secret passage.", 0.05)
    decision = input("Do you enter the passage or do not enter? (enter/do not enter): ")                                                   #asks for user input
    if decision.lower() == "enter":                                                                                                        #conditional statement
        print_with_delay("You decide to enter the passage.", 0.05)
        event10()                                                                                                                          #calls evemt10()
    elif decision.lower() == "do not enter":                                                                                               #conditional statement
        print_with_delay("You try to find more clues in the library but can't find any.", 0.05)
        print_with_delay("You decide to go back out of the door", 0.05)
        print_with_delay("As soon a you step outside of the room you see deadly snakes coming out of the cracks in the flooring", 0.05)
        print_with_delay("You try to run away", 0.05)
        print_with_delay("Unfortunately the snakes catch up to you", 0.05)
        print_with_delay("You Die.", 0.05)
        print_with_delay("Game Over!", 0.05)
        play_again()                                                                                                                       #calls play_again()
    else:                                                                                                                                  #conditional statement
        print_with_delay("Invalid choice. Please enter 'enter' or 'do not enter'.", 0.05)
        event9()                                                                                                                            #calls event9()

def event10():                                                                                                                              #defines event10()
    print_with_delay("You keep going deeper into the passage trying to find 'The Key' that you can use to escape the mansion.", 0.05)
    print_with_delay("In your exploration, you come across a mysterious locked chest.", 0.05)          
    decision = input("Do you try to pick the lock or keep moving forward? (pick lock/keep going): ")                                         #asks for user input
    if decision.lower() == "pick lock":                                                                                                      #conditional statement
        print_with_delay("You pick the lock and manage to open it.", 0.05)
        print_with_delay("Inside the box is a massive Time Bomb that is about to go off in a few seconds", 0.05)
        print_with_delay("3", 0.05)
        print_with_delay("2", 0.05)
        print_with_delay("1", 0.05)
        print_with_delay("The Bomb goes off, you die", 0.05)
        print_with_delay("Game over!", 0.05)
        play_again()                                                                                                                         #calls play_again()
    elif decision.lower() == "keep going":                                                                                                   #conditional statement
        print_with_delay("You keep moving forward in hopes of finding 'The Key'.", 0.05)
        print_with_delay("there is a deadend with a door in front of you.", 0.05)
        print_with_delay("You have no other choice but to enter the room", 0.05)
        event11()                                                                                                                            #calls event11()
    else:                                                                                                                                    #conditional statement
        print_with_delay("Invalid choice. Please enter 'pick lock' or 'keep going'.", 0.05)
        event10()                                                                                                                            #calls event10()

def event11():                                                                                                                               #defines event11()
    print_with_delay("You enetr the room.", 0.05)
    print_with_delay("You stumble upon an ancient laboratory filled with strange experiments and objects of the past!.", 0.05)
    decision = input("Do you investigate the experiments to search for clues or search for an exit? (investigate/search exit): ")            #asks for user input
    if decision.lower() == "investigate":                                                                                                    #conditional statement
        print_with_delay("You discover a small box containing notes, revealing the mansion's dark history.", 0.05)
        print_with_delay("It has the blueprint of the mansion", 0.05)
        print_with_delay("In other words, A Map! The Key to your escape!", 0.05)
        event12()                                                                                                                              #calls event12()
    elif decision.lower() == "search exit":                                                                                                    #conditional statement
        print_with_delay("You search for an exit and find a hidden passage.", 0.05)
        print_with_delay("The passage leads you back to where you came from.", 0.05)
        print_with_delay("You are faced with the same situation", 0.05)
        event8()                                                                                                                               #calls event8()
    else:                                                                                                                                      #conditional statement
        print_with_delay("Invalid choice. Please enter 'investigate' or 'search exit'.", 0.05)
        event11()                                                                                                                               #calls event11()


def event12():                                                                                                                                  #defines event12()
    print_with_delay("You examine the map carefully, and it shows a way to a hidden vault located in the deepest part of the mansion.", 0.05)
    print_with_delay("On the map there is a symbol of the KEY made where the vault is located, meaning that it could have could have the KEY to your survival", 0.05)
    print_with_delay("Following the map, you navigate through narrow passages and avoid various traps.", 0.05)
    print_with_delay("Finally, you reach what appears to be a hidden labyrinth.", 0.05)
    decision = input("Do you trust the map completely or trust your instincts? (trust map/trust instincts): ")                                  #asks for user input
    if decision.lower() == "trust map":                                                                                                         #conditional statement
        print_with_delay("You follow the map meticulously and navigate through the labyrinth.", 0.05)
        print_with_delay("After a while, you find a hidden door that leads to another secret passage.", 0.05)
        event13()                                                                                                                                #calls event13()
    elif decision.lower() == "trust instincts":                                                                                                  #conditional statement
        print_with_delay("Trusting your instincts, you decide to navigate the labyrinth on your own.", 0.05)
        print_with_delay("Unfortunately, you encounter a dead end filled with traps.", 0.05)
        print_with_delay("The walls close in, and you meet a grisly end.", 0.05)
        print_with_delay("Game over!", 0.05)
        play_again()                                                                                                                             #calls play again()
    else:                                                                                                                                        #conditional statement
        print_with_delay("Invalid choice. Please enter 'trust map' or 'trust instincts'.", 0.05)
        event12()                                                                                                                                #calls event12()

def event13():                                                                                                                                   #defines event13()
    print_with_delay("The secret passage leads you to an ancient chamber guarded by a mystical creature.", 0.05)
    print_with_delay("The guardian asks you a riddle: 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?'", 0.05)
    answer = input("What is your answer? ")                                                                                                      #asks for user input
    if answer.lower() == "echo":                                                                                                                 #conditional statement
        print_with_delay("The guardian nods and steps aside, revealing a staircase leading down.", 0.05)
        print_with_delay("You descend the staircase and find yourself in a hidden part of the mansion.", 0.05)
        event14()                                                                                                                                #calls event14()
    else:                                                                                                                                        #conditional statement
        print_with_delay("The guardian roars and attacks you for giving the wrong answer.", 0.05)
        print_with_delay("You fight bravely but are ultimately overpowered.", 0.05)
        print_with_delay("Game over!", 0.05)
        play_again()                                                                                                                             #calls play again()
        
def event14():                                                                                                                                   #defines event14()
    print_with_delay("You enter the deepest part of the mansion and find a hidden vault.", 0.05)
    print_with_delay("Inside the vault, you discover a key and several ancient artifacts.", 0.05)
    decision = input("Do you take only the key or examine the artifacts? (take key/examine artifacts): ")                                        #asks for user input
    if decision.lower() == "take key":                                                                                                           #conditional statement
        print_with_delay("You wisely decide to take only the key and avoid unnecessary distractions.", 0.05)
        print_with_delay("The key glows in your hand, and you feel a strange sense of hope.", 0.05)
        event15()                                                                                                                                 #calls event15()
    elif decision.lower() == "examine artifacts":                                                                                                 #conditional statement
        print_with_delay("As you examine the artifacts, you accidentally trigger a magical trap.", 0.05)
        print_with_delay("You are turned to stone.", 0.05)
        print_with_delay("Game over!", 0.05)
        play_again()                                                                                                                              #calls play_again()
    else:                                                                                                                                         #conditional statement
        print_with_delay("Invalid choice. Please enter 'take key' or 'examine artifacts'.", 0.05)
        event14()                                                                                                                                 #calls event14()

def event15():                                                                                                                                    #defines event15()
    print_with_delay("With the key in hand, you follow the map's final instructions to the mansion's main gate.", 0.05)
    print_with_delay("You encounter the same ghost that gave you clues in the beginning", 0.05)
    print_with_delay("As you look towards him, it vanishes into the air", 0.05)
    print_with_delay("You Reach the main gate and start opeing the lock", 0.05)
    print_with_delay("The key fits perfectly into the lock, and the gate creaks open.", 0.05)
    print_with_delay("You step outside into the fresh air, feeling the weight of the mansion lift off your shoulders and a great sense of joy.", 0.05)
    print_with_delay("You've escaped the haunted mansion!", 0.05)
    print_with_delay("Congratulations! You've won the game!", 0.05)
    play_again()                                                                                                                                 #calls play_again()


start_game()                                                                                                                                     #calls start_game()






    
    



