#program that randomly picks a name
import random
names=["tracy","joan","stacy","lilian","jack","ronny","wendy","ivy","ray","kyle"]
rand_name=random.choice(names)
print(f"Randomly selected name:{rand_name}")

#program that rolls two dices
import random
user=int(input("what do you side do you want to play?[1-6]\n"))
if 1 <= user <= 6:
   rand_dice=random.randint(1, 6)
   print(f"Dice rolled: {rand_dice}")

   if user == rand_dice:
    print("congrats!you guessed correctly") 

   else:
        print("Try again next time")
else:
    print("Invalid imput! Please a number between 1 and 6")        


# program for question generator
import random
pet=["cat","dog","mice"]
my_pet=input("what pet do you like?(cat,dog, mice) \n")
rand_pet=random.choice(pet) #randomly selects a pet
print(f"User's choice:{my_pet}")
print(f"Randomly selected pet:{rand_pet}")

if my_pet == rand_pet:
    print("Great choice !You and the random match")
else:
    print("Different choice ,Please try again")    