print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the hidden treasure.")
print("You are standing at the entrance of a dark cave.")
print("You can see two paths in front of you.")
print("Which path do you want to take?")
print("(A) Left path")
print("(B) Right path")
print("Type 'A' for left path or 'B' for right path: ")
choice=input().upper()
if choice=='B':
    print("You fell into a hole! Game over")
elif choice=='A':
    print("You see a glimmer of light in the distance.")
    print("You approach the light and find a lake! There is an island at the middle of the lake.")
    print("Type \"wait\" to wait for the boat. Type \"swim\" to swim across.")
    choice2=input().lower()
    if choice2=='swim':
        print("You were attacked by a sea monster! Game over")
    elif choice2=='wait':
        print("You wait for the boat and cross the lake.")
        print("There are three doors in front of you.Red, yellow and blue.")
        print("Which door do you want to open?")
        print("Type r for red, y for yellow, b for blue")
        choice3=input().lower()
        if choice3=='r':
            print("You were burned by fire! Game over")
        elif choice3=='b':
            print("You were eaten by beasts! Game over")
        elif choice3=='y':
            print("You found the treasure!")
            print("Suddenly, a guardian appears and askes you a riddle to prove your worth!")
            print("I can hold many secrets, yet I am often empty. I can be filled with knowledge, but I am not alive. What am I?")
            answer=input().lower()
            if answer=='book':
                print("You are worthy of the treasure!")
                print("YOU GOT THE TREASURE!")
            else:
                print("Wrong answer!")
                print("Guardian gives you second chance!")
                print("I am always in front of you but can’t be seen. What am I?")
                answer2=input().lower()
                if answer2=='future':
                    print("You are worthy of the treasure!")
                    print("YOU GOT THE TREASURE!")
                else :
                    print("Wrong answer!")
                    print("You are not worthy of the treasure!")
                    print("Game over!")
            print()
        else:
            print("Invalid choice. Game over")
    else:
        print("You must type either \"wait\" or \"swim\" to proceed.")
else:
    print("You must type either \"A\" or \"B\" to proceed.")