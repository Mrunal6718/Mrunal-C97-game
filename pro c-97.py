import random
print("numberguessinggame")
number=random.randint(1,9)
chances=0
print("guess a number between 1 and 9")
while chances<5:
    guess=int(input("enteryourguess"))
    if guess==number:
        print("congradulations you won")
        break
    elif guess<number:
     print("your guess was too low",guess)
    else:
     print("your guess is too high",guess)
    chances+=1