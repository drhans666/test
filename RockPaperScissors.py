import random
import sys
import os

ART = ['''
    
 _/----\     
/rock_' \ 
| \   \ |
 \  \_/ /
  \_-__/ ''',

'''

 _______
/      |
|paper |
|      |
-------/''',

'''

scissors
 \ /
  X
 / \ 
O   O''']




def getPlayerChoice():

    while True:
        print('Make you choice: paper, rock, scissors')
        chosenWeapon = input()
        chosenWeapon = chosenWeapon.lower()

        if chosenWeapon not in weapons:
            print()
        else:
            choice = weapons.index(chosenWeapon)

            break
    return choice


def getComputerChoice():
    choice2 = random.randint(0, len(weapons) - 1)

    return choice2


def assignChoicesToArena(arena,choice,choice2):
    arena.append(choice)
    print('Player:', ART[choice])
    arena.append(choice2)
    print('Computer:', ART[choice2])
    arena = []
    return arena





def choiceConfront(arena,playerPoints, computerPoints):

    if arena == [0, 0]:
        print('draw')
    elif arena == [0, 1]:
        print('paper wins')
        computerPoints += 1
    elif arena == [0, 2]:
        print('rock wins')
        playerPoints += 1
    elif arena == [1, 0]:
        print('paper wins')
        playerPoints += 1
    elif arena == [1, 1]:
        print('draw')
    elif arena == [1, 2]:
        print('scissors wins')
        computerPoints += 1
    elif arena == [2, 0]:
        print('rock wins')
        computerPoints += 1
    elif arena == [2, 1]:
        print('scissors wins')
        playerPoints += 1
    elif arena == [2, 2]:
        print('draw')


    return playerPoints, computerPoints


def playAgain():

    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

os.system('clear')
weapons = ['rock', 'paper', 'scissors']
playerPoints = 0
computerPoints = 0

while True:
    arena = []
    playerPoints = choiceConfront(arena,playerPoints, computerPoints)
    computerPoints = choiceConfront(arena,playerPoints, computerPoints)
    choice = getPlayerChoice()
    choice2 = getComputerChoice()
    assignChoicesToArena(arena, choice, choice2)
    choiceConfront(arena, playerPoints, computerPoints)
    print('Player Points:',playerPoints)
    print('Computer Points:', computerPoints)

    if playerPoints == 3:
        print('Congratulations, You won!')
    elif computerPoints == 3:
        print('You Lost. Better Luck Next Time!')
        break

    playAgain()

sys.exit()