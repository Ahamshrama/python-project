import random

i = 0
while i < 3:
    a = random.randint(1 , 10)
    b = int(input("Enter any number . . . "))
    if a == b:
        print("Yeh! u won the game")
        print("u guessed ",a ," ","and random generted is ", " ", b , " ", " both are equals . . . .")
        break
    else:
        print("Try Again because random generated number was :- " , a)
    i += 1
print("Your turns are over")