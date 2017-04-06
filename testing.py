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

weapons = ['rock', 'paper', 'scissors']

arena = []


#player choses weapon + assignation to arena
while True:
    print('Make you choice: rock, paper, scissors')
    chosenWeapon = input()
    chosenWeapon = chosenWeapon.lower()

    if chosenWeapon not in weapons:
        print()
    else:
        choice = weapons.index(chosenWeapon)
        arena.append(choice)
        print('Player:', ART[choice])
        break

#computer weapon randomly assigned to arena
choice2 = random.randint(0, len(weapons) -1)
arena.append(choice2)
print('Computer:', ART[choice2])

#what weapones do to each other (0-rock, 1-paper, 3-scissors
playerPoints = 0
computerPoints = 0

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
print(arena)

print(playerPoints)
print(computerPoints)
