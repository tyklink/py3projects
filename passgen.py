import random
import time
import sys
lowerlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
speclist = []
print('Welcome to the random password generator!')
while True:
    try:
        char = int(input('How many characters do you want? '))
    except ValueError:
        print('That is not a number.')
        continue
    if char <= 0:
        print('Please put in a real number.')
        continue
    else:
        break
while True:
    lowerw = input('Do you want lower case letters? (y/n) ')
    if lowerw == 'y':
        break
    if lowerw == 'n':
        break
    else:
        print('Please choose \"y\" or \"n\".')
        continue
while True:
    upperw = input('Do you want upper case letters? (y/n) ')
    if upperw == 'y':
        break
    if upperw == 'n':
        break
    else:
        print('Please choose \"y\" or \"n\".')
        continue
while True:
    numw = input('Do you want numbers? (y/n) ')
    if numw == 'y':
        break
    if numw == 'n':
        break
    else:
        print('Please choose \"y\" or \"n\".')
        continue
while True:
    specialw = input('Do you want to add any custom special characters? (y/n) ')
    if specialw == 'y':
        print('You can add as many special characters as you want.')
        print('Type \"finish\" at any time when completed.')
        while True:
            specadd = str(input('Character: '))
            if specadd == 'finish':
                break
            else:
                speclist.append(specadd)
                continue
        break
    if upperw == 'n' and lowerw == 'n' and numw == 'n' and specialw == 'n':
        sys.exit('Well fine, I won\'t generate one for you.')
    if specialw == 'n':
        break
    else:
        print('Please choose \"y\" or \"n\".')
        continue
print('Generating your requested password...')
time.sleep(3)
charcount = 0
charchoice = []
if lowerw == 'y':
    charchoice.append('L')
if upperw == 'y':
    charchoice.append('U')
if numw == 'y':
    charchoice.append('N')
if specialw == 'y' and speclist != []:
    charchoice.append('S')
char += 1
password = ''
while True:
    charcount += 1
    if charcount == char:
        break
    passchar = str(random.choice(charchoice))
    while True:
        if passchar == 'L':
            passrnd = str(random.choice(lowerlist))
            password += passrnd
            break
        if passchar == 'U':
            passrnd = str(random.choice(upperlist))
            password += passrnd
            break
        if passchar == 'N':
            passrnd = str(random.choice(numlist))
            password += passrnd
            break
        if passchar == 'S':
            passrnd = str(random.choice(speclist))
            password += passrnd
            break
print('Here is your password:')
print(password)