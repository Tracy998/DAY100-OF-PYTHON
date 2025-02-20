# #Program that checks if a number is odd or even using the modulus operator
# numb1=int(input("what is the first number?"))
# if numb1 % 2 == 0: # modulus operator
#     print("even number")
# else:
#     print("odd number")    


# # Movie ticket pricing system
# age=int(input("What is your age?"))
# print(age)
# bill=0
# if age >=18:
#     bill += 1000
# elif age <= 12:
#      bill += 500
# elif age >= 12 and age <=18 :
#      bill += 700

# print(f"Your ticket price is Ksh {bill}.")   

# #Program for password strength Checker
# passkey=input("What is the password of your email?")
# print(passkey)
# if

# #program for Even or odd Game 
# numb1=int(input("what is the first number?"))

# if numb1 == 0 :
#      print("Zero is neither even or odd!")
# elif numb1 %  5 == 0:     
#     print("Special number")    
# elif numb1 % 2 == 0:     
#     print("Even  number")
# else:
#      print ("Odd number") 


# # Challenge 2 program for simple coin toss game
# import random
# coins=["Head" ,"Tail"]
# Toss_game=int(input("which side do you prefer? Type 0 for Head or  1 for Tail \n"))
# rand_toss= random.randint(0,1)
# # print(coins[rand_toss])
# if Toss_game == 0:
#      print("Head")
# elif Toss_game == 1:
#      print("Tail")
# else:
#      print("An error message ,stop the")          

 #program for simple math quiz game
import random
operator=int(input("Which operation do you prefer? Type 1 for + , 2 for - ,3 for * or 4 for /\n"))
rand_mat1=random.randint(1,20) 
rand_mat2=random.randint(1,20) 
rand_mat3=random.randint(1,20)
rand_mat4=random.randint(1,20)
if operator == 1:
    answer= rand_mat1 + rand_mat2
elif operator == 2:
     answer = rand_mat1 -rand_mat2
elif operator == 3:
     answer = rand_mat1 * rand_mat2    
elif operator == 4:
     answer = rand_mat1 / rand_mat2    
else:
    print("Invalid please select 1,2,3 or 4")
    exit()
user_predict = int(input(f"what is your{rand_mat1} {operator} {rand_mat4} \n"))    
 
if user_predict == answer:
    print("correct!")
else :
    print(f"Wrong answer !The correct answer was: {answer}")    
   
      
