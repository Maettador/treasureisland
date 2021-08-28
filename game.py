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

way = input("You are starting at a crossroad with two ways. Which way do you choose, left or right? ")
way_ = way.lower()

if way_ == "right":
  print("You fell into a hole and died. Game Over.")
else:
  lake = input("You arrive at a lake. Will you wait or swim? ")
  lake_ = lake.lower()
  if lake_ == "swim":
    print("You drowned in the lake. Game Over.")
  else:
    print("After a while, a boat came and brought you to the other side.")
    doors = input("You are now standing in front of a yellow, blue and red door. Which one will you open? ")
    doors_ = doors.lower()
    if doors_ == "red":
      print("You got killed by a burst of fire. Game Over.")
    elif doors_ == "yellow":
      print("You breathed in a poison cloud and died. Game Over.")
    else:
      print("You found the treasure. Good fortune!")
