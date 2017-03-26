lista = [
    [1, 11, 111],
    [2, 22, 222],
    [3, 33, 333],
    [4, 44, 444],
    [5, 55, 555],
]

for wiersz in lista:
    for komorka in wiersz:
        print(komorka)

for i, wiersz in enumerate(lista):
    for j, komorka in enumerate(wiersz):
        print(i, j, komorka)

for i in range(0, len(lista)):
    for j in range(0, len(lista[i])):
        print(lista[i][j])

for nr_kolumny in range(0, 3):
    for nr_wiersza in range(0, 5):
        print(lista[nr_wiersza][nr_kolumny])
