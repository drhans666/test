import sys
import time

def parasiteY(paraY):
    if paraY < axisY:
        paraY += 1
    elif paraY == axisY:
        paraY += 0

    else:
        paraY -= 1

    return paraY

def parasiteX(paraX):
    if paraX <= axisX:
        paraX += 1
    elif paraX == axisX:
        paraX +=0

    else:
        paraX -= 1
    return paraX

def clash():
    if axisX == paraX:
        if axisY == paraY:
            print("You're Dead!!")
            sys.exit()


import os
zone = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
        ['|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '|'],
        ['|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '|'],
        ['|', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'E', '|'],
        ['|', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'X', '|'],
        ['|', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'I', '|'],
        ['|', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'T', '|'],
        ['|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '|'],
        ['|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '|'],
        ['|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '|'],
        ['|', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '|'],
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]


#displays intro with moving object in the center
def introScreen():
    print('Welcome To PARASITE'.center(50, '='))
    time.sleep(2)
    print("Reach The Exit. Don't Get Killed ".center(50, '='))
    time.sleep(2)
    print("He will follow. ".center(50, '='))
    time.sleep(2)
    print('''Controls:
     789
     456
     123''')
    time.sleep(3)
    zone[axisY][axisX] = 'O'
    zone[paraY][paraX] = '?'
    for i in zone:
        print(i)
    zone[axisY][axisX] = '.'
    zone[paraY][paraX] = '.'


def movement(coord, axisX, axisY):
    if coord == '8':
        axisY -= 1
    elif coord == '2':
        axisY += 1
    elif coord == '4':
        axisX -= 1
    elif coord == '6':
        axisX += 1
    elif coord == '9':
        axisX += 1
        axisY -= 1
    elif coord == '7':
        axisX -= 1
        axisY -= 1
    elif coord == '3':
        axisX += 1
        axisY += 1
    elif coord == '1':
        axisX -= 1
        axisY += 1
    return axisX, axisY

#Limits horizontal movement in zone
def limitY(axisY):
    while True:
        if axisY == limitMin:
            axisY += 1
        elif axisY == limitMax:
            axisY -= 1
        else:
            break
    return axisY

#Limits vertical movement in zone
def limitX(axisX):
    while True:
        if axisX == limitMin:
            axisX += 1
        elif axisX == limitMax:
            axisX -= 1
        else:
            break
    return axisX




paraY = 7
paraX = 10
axisY = 3
axisX = 1
limitMin = 0
limitMax = len(zone) - 1
os.system('clear')
introScreen()

while True:
    print('Your Move:')
    coord = input()

    os.system('clear')
    axisX, axisY = movement(coord, axisX, axisY)
    axisY = limitY(axisY)
    axisX = limitX(axisX)
    paraY = parasiteY(paraY)
    paraX = parasiteX(paraX)
    clash()
    zone[axisY][axisX] = 'O'
    zone[paraY][paraX] = '?'
    for i in zone:
        print(i)


    zone[axisY][axisX] = '.'
    zone[paraY][paraX] = '.'
