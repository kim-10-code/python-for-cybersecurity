def guess_the_number():
    import random 
    secret_number = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20')

    for guesses_taken in range(1, 7):
        print('Take a guess')
        guess = int(input())

        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            break

    if guess == secret_number:
        print('Good job, you guessed my number in ' + str(guesses_taken) + ' guesses')
    else:
        print('Nope, the number I was thinking of was ' + str(secret_number))

def rock_paper_scissors():
    import random, sys
    print('ROCK, PAPER, SCISSORS')

    wins = 0
    loses = 0
    ties = 0

    while True:
        print('%s Wins, %s Losses, %s Ties' % (wins, loses, ties))
        while True:
            print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
            player_move = input()
            if player_move == 'q':
                sys.exit()
            if player_move == 'r' or player_move == 'p' or player_move == 's':
                break

        if player_move == 'r':
            print('ROCK VS ...')
        elif player_move == 'p':
            print('PAPER VS ...')
        elif player_move == 's':
            print('SCISSORS VS ...')

        random_numer = random.randint(1,3)

        if random_numer == 1:
            computer_move = 'r'
            print('ROCK')
        elif random_numer == 2:
            computer_move = 'p'
            print('PAPER')
        elif random_numer == 3:
            computer_move = 's'
            print('SCISSORS')

        if player_move == computer_move:
            print('It is a tie!')
            ties = ties + 1
        elif player_move == 'r' and computer_move == 's':
            print('You win')
            wins = wins + 1
        elif player_move == 'p' and computer_move == 'r':
            print('You win')
            wins = wins + 1
        elif player_move == 's' and computer_move == 'p':
            print('You win')
            wins = wins + 1
        elif player_move == 'r' and computer_move == 'p':
            print('You lose!')
            loses = loses + 1
        elif player_move == 'p' and computer_move == 's':
            print('You lose!') 
            loses = loses + 1
        elif player_move == 's' and computer_move == 'r':
            loses = loses + 1

def spam():
    spam = 0
    if spam == 10:
        print('eggs')
        if spam > 5:
            print('bacon')
        else:
            print('ham')
        print('spam')
    elif spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    else:
        print('Greetings!')    
    print('spam')    

def for_loop():
    for i in range(10):
        print(i+1)

    i = 1
    while i <= 10:
        print(i)
        i = i + 1

def __init__():
    for_loop()

__init__()
# print((5>4) and (3==5))
# print(not (5 > 4))
# print((5 > 4) or (3==5))
# print((True and True) and (True == False))
# print((not False) or (not True))



