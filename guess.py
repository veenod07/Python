'''name = input(enTER PLAYER1 name) 
n(secret number) = random 1 to 99
guess = user ko guess 
loop n != equal
 guess < n
 print(user entered number is less than secret number)
 guess 
 guess > n
 print(user enter number is bigger than the secret number)

 else if guess == 0
 print(u have pressed 0 and u exited the game)

 else
 print(name," you have guessed it correct")
 '''

import random

name = input("enter player1 name ")
n = random.randint(1,99) # 45
guess = int(input("guess the number ")) #34

while n != guess:  #45 != 45
    if guess < n:
        print("your number ",guess,"  is less than secret nnumber")
        guess = int(input("enter your new guess ")) #45
    elif guess > n:
        print("your number ",guess," greater than secret nnumber")
        guess = int(input("enter your new guess "))
    
        
print("congo ",name," you got the number") 
print("secret number was ",n)
