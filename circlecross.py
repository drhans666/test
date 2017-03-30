# -*- coding: utf-8 -*-
import os
import sys
import random
os.system('cls')

def select_area1():
    while True:
        area1 = raw_input("Player1: Enter area coordination for example a1, b3: ")

        if len(area1) != 2:
            print 'Area coordination consists of two characters: letter and number '
            continue
        return area1

def select_area2():
    while True:
        area2 = raw_input("Player 2: Enter area coordination for example a1, b3: ")

        if len(area2) != 2:
            print 'Area coordination consists of two characters: letter and number '
            continue
        return area2

def main():
    os.system('cls')
    print 'Hello, welcome to BLABLABLA!'

    a = [1, 2, 3]
    b = [1, 2, 3]
    c = [1, 2, 3]

    if __name__ == '__main__':

    main()
    return