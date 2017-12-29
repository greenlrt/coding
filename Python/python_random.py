from random import randint

answer = randint(1, 10)
tries = 0

while tries < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == answer:
        print "YOU WIN!!!"
        break
    else:
        print "Try again"
        tries = tries + 1

print "Game Over"

print "The answer was " + str(answer)
