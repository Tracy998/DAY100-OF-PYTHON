print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
island=input("where do you want to head? (L)eft, (R)ight .\n") .upper() # to specify the output should be upper nonetheless the journey will end

if island == "L":
     side =input ("which option will you prefer (S)wim,(W)ait .\n") .upper()

     if side == "S":
        print("Attacked by trout!,meet with the trout")
        Chain = input("What happened ? (KILLED THE TROUT) Or (ATTACKED BY THE TROUT).\n") .upper()

        if Chain == "KILLED THE TROUT":
            print ("You survived the attack")
        elif Chain == "ATTACKED BY THE TROUT":
             print ("You were attacked ,Game over!")
        else:
             print("Attacked by the trout, Game over!")
     elif side == "W":
        Door = input("What colour of the door do you prefer? (B)lue , (R)ed, (Y)ellow .\n").upper()
        if Door == "B":
            print("Eaten by beasts .Game over.")
        elif Door == "R":
            print("Burned by fire. Game over")
        elif Door == "Y":
            print("You win!")
else:
    print ("Fall into a hole.Game over!")
