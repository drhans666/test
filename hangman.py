# -*- coding: utf-8 -*-
import sys
import random
os.system('cls')
print 'WITAJ W MOJEJ WERSJI HANGMAN. UWAGA PRODUKT RAKOTWORCZY'

slowo = random.choice(['samolot', 'kelnerka', 'komputer', 'makaron', 'motor', 'transport' ])

def pobieranie_i_weryfikacja():


    while True:

        litera = raw_input("Wpisz pojedyncza litere: ")




        # walidacja
        if len(litera) != 1:
            print 'miala byc jedna litera'
            continue
        break

    return slowo, litera,


def main():
    zycia = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    #odpowiedzialne za zliczanie trafien
    odganiete = 0
    #odpowiedzialna za wyswietlanie trafien
    trafiona = ' '
    #przechowuje odgadniete litery
    powtorki = []


    while True:
        slowo, litera = pobieranie_i_weryfikacja()
        #wszystkie skutki pomylek
        if litera not in slowo:
            del zycia[1]
            print 'BRAK WYSTAPIEN. POZOSTALO', len(zycia) - 1, 'ZYC'
        #odejmowanie zyc za powtarzanie liter
        if litera in powtorki:
            del zycia[1]
            print 'BYLO. NIE MA CWANIAKOWANIA. POZOSTALO', len(zycia) - 1, 'ZYC'

            if len(zycia) == 1:
                print
                sys.exit('przegrales')

            continue

        # wykonanie
        trafiona += litera
        #dodanie liter do listy poprawnie odgadnietych
        if litera in slowo:
            powtorki.append(litera)
        print slowo.count(litera), ('wystapienia')
        odganiete = odganiete + slowo.count(litera)
        #wypisywanie zgadnietych liter
        for char in slowo:
            if char in trafiona:
                print char

            else:

                print '.'

        if odganiete >= len(slowo):
            print 'ODGADLES. GRATULUJE'
            exit()


if __name__ == '__main__':
    # uruchom glowny program tylko jak ten skrypt jest odpalony z python a nie importowany z innego pliku
    main()