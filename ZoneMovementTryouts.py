import os
zone = [['-', '-', '-', '-', '-', '-', '-'],
        ['|', '.', '.', '.', '.', '.', '|'],
        ['|', '.', '.', '.', '.', '.', '|'],
        ['|', '.', '.', '.', '.', '.', '|'],
        ['|', '.', '.', '.', '.', '.', '|'],
        ['|', '.', '.', '.', '.', '.', '|'],
        ['-', '-', '-', '-', '-', '-', '-']]


#displays intro with moving object in the center
def introScreen():
    zone[axisY][axisX] = 'O'
    for i in zone:
        print(i)
    zone[axisY][axisX] = '.'

#vertical movement
def movementY(coord, axisY):
    if coord == 'up':
        axisY -= 1
    elif coord == 'down':
        axisY += 1
    return axisY

#horizontal movement
def movementX(coord, axisX):

    if coord == 'left':
        axisX -= 1
    elif coord == 'right':
        axisX += 1
    return axisX
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





axisY = 3
axisX = 3
limitMin = 0
limitMax = len(zone) - 1
os.system('clear')
introScreen()

while True:
    print('Type Your direction: up, down, left, right')
    coord = input()

    os.system('clear')
    axisY = movementY(coord, axisY)
    axisX = movementX(coord, axisX)
    axisY = limitY(axisY)
    axisX = limitX(axisX)

    zone[axisY][axisX] = 'O'

    for i in zone:
        print(i)


    zone[axisY][axisX] = '.'

