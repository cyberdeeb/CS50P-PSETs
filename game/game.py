import random

# Loop till valid level is given
while True:
    try:
        level = int(input('Level: '))
        if level > 0:
            break
    except:
        pass

def game():
    # Random number generator up to level set
    randomNum = random.randint(0,level)

    # Loop till valid guess is given and check
    while True:
        try:
            guess = int(input('Guess: '))
            if guess > 0:
                if randomNum > guess:
                    print('Too small!')
                elif randomNum < guess:
                    print('Too large!')
                else:
                    print('Just right!')
                    break
        except:
            pass



game()



