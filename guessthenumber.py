import random
answer = random.choice(range(1, 101))
guess = 0
guesses = 0
print('I am thinking of a random integer between 1 and 100.')
print('Use the process of elimination to guess what it is!\nEnter the number 0 to give up :(')
while guess != answer:
    guess = int(input('Guess a number: '))
    guesses += 1
    if guess == 0:
        print('Quitter.')
        break
    elif guess > answer:
        print('Lower!')
    elif guess < answer:
        print('Higher!')
    elif guess == answer:
        print('Correct! Only ' + str(guesses) + ' tries!')
        break
