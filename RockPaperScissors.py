import random

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

def assignChoicesToArena(choice, choice2, arena):
    arena.append(choice)
    print('Player:', ART[choice])
    arena.append(choice2)
    print('Computer:', ART[choice2])
    return choice, choice2, arena

def choiceConfront():
    if arena == [0, 0]:
        print('draw')
    elif arena == [0, 1]:
        print('paper wins')
    elif arena == [0, 2]:
        print('rock wins')
    elif arena == [1, 0]:
        print('paper wins')
    elif arena == [1, 1]:
        print('draw')
    elif arena == [1, 2]:
        print('scissors wins')
    elif arena == [2, 0]:
        print('rock wins')
    elif arena == [2, 1]:
        print('scissors wins')
    elif arena == [2, 2]:
        print('draw')



def playAgain():

    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

weapons = ['paper', 'rock', 'scissors']
arena = ()


getPlayerChoice()
getComputerChoice()
assignChoicesToArena(choice2,arena)
