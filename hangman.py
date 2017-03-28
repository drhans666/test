# -*- coding: utf-8 -*-
import os
import sys
import random
os.system('cls')


def pobieranie_i_weryfikacja():

    slowo = 'transport'
    while True:
        litera = raw_input("Wpisz pojedyncza litere: ")

        # liczy czy faktycznie została wpisana pojedyncza litera

        # walidacja
        if len(litera) != 1:
            print 'miala byc jedna litera'
            continue
        break

    return slowo, litera,


def main():
    zycia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odganiete = 0
    while True:
        slowo, litera = pobieranie_i_weryfikacja()
        #wszystkie skutki pomylek
        if litera not in slowo:
            del zycia[1]
            print '0 wystapien. idz umrzyj'
            print ('POZOSTALO', len(zycia), 'ZYC')
            if len(zycia) < 1:
                sys.exit('Przegrales')
            continue

        # wykonanie
        print 'brawo'
        print slowo.count(litera), ('wystapienia')
        odganiete = odganiete + slowo.count(litera)
        if odganiete >= len(slowo):
            print 'wygrales'
            exit()


if __name__ == '__main__':
    # uruchom glowny program tylko jak ten skrypt jest odpalony z python a nie importowany z innego pliku
    main()


#Do zrobienia:
#1. losowe wybieranie słów
#2. wyswietlanie odgadnietych liter
#3. brak możliwości ponownego odgadniecia litery
#4. Powiazac grafike wisielca z iloscia zyc