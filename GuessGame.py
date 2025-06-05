#This is a guess game 

import random 

# randomizing my secret number 
secretNumber = random.randint(1, 20)
print(
      'I am thinging of a number between 1 and 20')

#limiting the guess to 6 
for guessTaken in range(1,7):
    guess = int(input('Take a guess...'))
    
    if guess < secretNumber:
        print('Give it another try, your guess is too low...')
    elif guess > secretNumber:
        print('Hey, you are almost there. Try something lower...')
    else: 
        break #This is the right guess 

if guess == secretNumber:
    print('Bravo.. You guessed my number in ' + str(guessTaken))
else:
    print('Oh, my number is ' + str(secretNumber))


