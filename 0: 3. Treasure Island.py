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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("Your at a crosswalk.")
first_step = input("Do you go left or right?\n")
if first_step == "left":
    print("Great choise! Keep going.\n Your at a river and you need to cross it. You can swim but there are sharks. You can also wait on a boat which will arrive in three years. What do you do?")
    second_step = input("Do you want to swim or wait?\n")
    if second_step == "wait":
        print("Your on a roll. Keep it up!\n The treasure is almost in reach. But this will be your toughest choise yet. Their are three doors. Yellow, Red and Blue.")
        final_step = input("Which one do you go through?\n")
        if final_step == "yellow":
            print("Congratulations! You've won a treasure of one gejillion dollars!")
        else:
            print("Game Over!")
    else:
        print("Game Over!")
else:
    print("Game Over!")
