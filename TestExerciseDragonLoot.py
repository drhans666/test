

def displayInventory(inv):
    print('inventory:')
    item_total = 0
    for item, numbers in inv.items():
        print (str(numbers) + ' ' + item)
        item_total += numbers
    print('Total items: ' + str(item_total))

def addToInventory(inv, dragonLoot):
    for i in dragonLoot:
        if i in inv:
            inv[i] = inv[i] + 1
        if i not in inv:
            inv.setdefault(i, 1)

    return(inv)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

