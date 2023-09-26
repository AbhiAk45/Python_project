import random

def guess(x):
    random_number = random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f'Guess a number between 1 and {x}: '))
        if guess< random_number:
            print('sorry guess again.too low')
        elif guess>random_number:
            print('guess is too high guess again ')
        

    print(f'yay , congrats. you have guessed the number {guess} correctly !!.')

guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback= ''
    while feedback!='C':
        guess=random.randint(low, high)
        feedback= input(f"Is {computer_guess} too high(H),too low (L), or correct (C)??").lower() 
        if feedback == 'h':
            high= guess-1
        elif feedback== 'l':
            low = guess + 1
        else:
         print(f'yay your computer got your number,{guess}, correctly!')

computer_guess(10)