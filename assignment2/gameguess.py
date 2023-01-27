import random
digits=random.randrange(1, 10)
userInput=int(input("Guess a Number"))
if userInput > digits:
    print("Computer Number")
    print(digits)
    print(" You've guessed a correct number but in the wrong position") 
elif userInput==digits:
    print("Computer Number")
    print(digits)
    print("You haven't guess any of the numbers correctly")  
else:      
    print("Computer Number")
    print(digits)
    print("You've guessed a correct number in the correct position")