
zone = [['.', '.', '.', '.', '.', ],
        ['.', '.', '.', '.', '.', ],
        ['.', '.', '.', '.', '.', ],
        ['.', '.', '.', '.', '.', ],
        ['.', '.', '.', '.', '.', ]]


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



axisY = 2
axisX = 2

introScreen()

while True:

    print('Type Your direction: up, down, left, right')
    coord = input()
    axisY = movementY(coord, axisY)
    axisX = movementX(coord, axisX)

    zone[axisY][axisX] = 'O'
    for i in zone:
        print(i)


    zone[axisY][axisX] = '.'

