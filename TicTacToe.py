import random

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

def showBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def isSpaceFree(board, move):
    return board[move] == ' '

def playerTurn(move):
    move = input()
    theBoard[move] = turn
    return move

def computerTurn(move):
    edges = ['1', '3', '7', '9']
    sides = ['2', '4', '6', '8']
    center = '5'
    if isSpaceFree:
        compMove = (random.choice(edges))


    theBoard[compMove] = 'O'
    return compMove
turn = 'X'
for i in range(9):
    showBoard(theBoard)
    while True:
        print('Move which space?')
        playerTurn()
        computerTurn()
        showBoard(theBoard)