#Program for a game of guessing numbers
import random
rand_guess=random.randint(1,10)
guess_Num=int(input("Guess a number between{rand_guess}?"))
if guess_Num == 1 or guess_Num == 10:
     print("Congratulations! you guessed it right!")

elif guess_Num > 10:
    print("Too high! Try again!")
elif guess_Num < 1:
     print("Too low ! Try again")    
else:
     print("Invalid guess ")