from random import randrange
from termcolor import colored
from time import time

startTime = time()
count = 0
countWinPlayerOne, countWinPlayerTwo, countLosePlayerOne, countLosePlayerTwo, countTie = 0, 0, 0, 0, 0
isFinished = None
playAgain = 'yes'


def convertSecondToTime(second):
    Minutes = 0
    Hour = 0
    while(True):
        Hour = second // 3600
        second %= 3600
        Minutes = second // 60
        second %= 60
        break
    print('Time of Program is: %d:%02d:%02d' % (Hour, Minutes, second))


def display():
    for i in range(len(game)):
        for j in range(len(game)):
            print(game[i][j], end=' ')
        print(' ')
    print('\n')


def checkRowCol(chosenMark, player):
    while True:
        if player == playerOne or player == playerTwo:
            if player == playerOne:
                row = int(input(f'{player} choose "row" :'))
                col = int(input(f'{player} choose "col" :'))
                print('\n')
            elif player == 'System':
                print('System Turn\n')
                row = randrange(0, len(game))
                col = randrange(0, len(game))
                while game[row][col] == X or game[row][col] == O:
                    row = randrange(0, len(game))
                    col = randrange(0, len(game))
            elif player == playerTwo:
                row = int(input(f'{player} choose "row" :'))
                col = int(input(f'{player} choose "col" :'))
                print('\n')
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == '_':
                game[row][col] = chosenMark
                global count
                count += 1
                display()
                break
            else:
                print('This cell is not empty!')
        else:
            print('Index out of range , please try again!')
    return


def checkWinner(isFinished):
    for i in range(3):
        # Row and Col
        if (game[i][0] == X and game[i][1] == X and game[i][2] == X) or (game[0][i] == X and game[1][i] == X and game[2][i] == X):
            print(f'{playerOne} you win!\n')
            isFinished = True
        if (game[i][0] == O and game[i][1] == O and game[i][2] == O) or (game[0][i] == O and game[1][i] == O and game[2][i] == O):
            print(f'{playerTwo} you win!\n')
            isFinished = True
            # Diameter
    if (game[0][0] == X and game[1][1] == X and game[2][2] == X) or (game[0][2] == X and game[1][1] == X and game[2][0] == X):
        print(f'{playerOne} you win!\n')
        isFinished = True
    if (game[0][0] == O and game[1][1] == O and game[2][2] == O) or (game[0][2] == O and game[1][1] == O and game[2][0] == O):
        print(f'{playerTwo} you win!\n')
        isFinished = True
    return isFinished


def checkTie(count):
    if count == len(game) * len(game):
        print(colored('No one Win , Game is Tie!\n', 'red', attrs=['bold']))
        return True


def showScoreBoard(*args):
    print(colored('-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n', 'blue'))
    print(f'Result of match for {playerOne}: \n')
    print(
        f'Count of Win is: {countWinPlayerOne}\nCount of Tie is: {countTie}\nCount of Lose is: {countLosePlayerOne}\n')
    print(colored('-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n', 'magenta'))
    print(f'Result of match for {playerTwo}: \n')
    print(
        f'Count of Win is: {countWinPlayerTwo}\nCount of Tie is: {countTie}\nCount of Lose is: {countLosePlayerTwo}\n')
    print(colored('-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|\n', 'yellow'))
    print(
        f'Total Played is: {countWinPlayerOne + countWinPlayerTwo + countTie}')
    return


# Main
selectMode = int(input(
    'For play "With System" enter 0\nFor play "With Another Player" enter 1\n\nPlease Enter: '))

if selectMode == 0:
    playerOne = input('Enter your name: ')
    print('\n')
    playerTwo = 'System'
elif selectMode == 1:
    playerOne = input('Player 1 enter your name: ')
    playerTwo = input('Player 2 enter your name: ')
    print('\n')

X = colored('X', 'red')
O = colored('O', 'green')

# Beginning of the Game
while playAgain == 'yes':
    game = [['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']]
    count = 0

    # With System
    if selectMode == 0:
        display()
        while True:
            # Player One
            checkRowCol(X, playerOne)
                if checkWinner(isFinished) == True:
                    countWinPlayerOne += 1
                    countLosePlayerTwo += 1
                    showScoreBoard(playerOne, playerTwo,
                                    countWinPlayerOne, countLosePlayerTwo)
                break
            if checkTie(count) == True:
                countTie += 1
                showScoreBoard(playerOne, playerTwo, countTie)
                break
                # Player Two or System
                    checkRowCol(O, playerTwo)
            if checkWinner(isFinished) == True:
                countWinPlayerTwo += 1
                countLosePlayerOne += 1
                showScoreBoard(playerOne, playerTwo,
                                countWinPlayerTwo, countLosePlayerOne)
                break
            if checkTie(count) == True:
                        countTie += 1
                showScoreBoard(playerTwo, playerOne, countTie)
                    break
    # Multiple Player
    elif selectMode == 1:
        display()
        while True:
            # Player One
            checkRowCol(X, playerOne)
            if checkWinner(isFinished) == True:
                    countWinPlayerOne += 1
                    countLosePlayerTwo += 1
                showScoreBoard(playerOne, playerTwo,
                                countWinPlayerOne, countLosePlayerTwo)
                break
            if checkTie(count) == True:
                    countTie += 1
                    showScoreBoard(playerOne, playerTwo, countTie)
                    break
            # Player Two
            checkRowCol(O, playerTwo)
            if checkWinner(isFinished) == True:
                countWinPlayerTwo += 1
                countLosePlayerOne += 1
                showScoreBoard(playerOne, playerTwo,
                                countWinPlayerTwo, countLosePlayerOne)
                break
            if checkTie(count) == True:
                countTie += 1
                showScoreBoard(playerTwo, playerOne, countTie)
                break
    # Ask for continuing the game or finish it.
    print(colored('##########################################################################\n', 'red'))
    playAgain = input(
        'Enter "Yes" if you want play again,if you dont please enter "No" :')
    print(colored('\n##########################################################################\n', 'green'))
    if playAgain.lower() == 'no':
        break
    elif playAgain.lower() == 'yes':
        continue
    else:
        while True:
            print(colored('\nPlease enter "YES" or "NO"\n',
                            'cyan', attrs=['bold', 'underline']))
            playAgain = input(
                '\nEnter "Yes" if you want play again,if you dont please enter "No":')
            if playAgain.lower() == 'yes' or playAgain.lower == 'no':
                break

print('\n')
# Time Computing
timeComputing = time() - startTime
convertSecondToTime(timeComputing)
