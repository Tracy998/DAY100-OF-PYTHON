# for loop practice to print first ten numbers in fib
fib_sequence= [0,1]
for series  in range(8):
    next_number =fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_number)

print("first 10 Fibonacci numbers:",fib_sequence)


# printing characters in word using for loop  
word=input("what word do you prefer? tracy, korir \n").lower()
for letter in word:
    print(letter)

#printing even numbers 
for numbers in range (1,101):
   
     if numbers % 2 == 0:
    
       print("even numbers are:",numbers)        
