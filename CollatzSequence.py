
def collatz(number):
    if number % 2 == 0:
        print('even')
        return number // 2
    else:
        print('odd')
        return 3 * number + 1



print('Enter number:')
number = int(input())
collatzOutput = collatz(int(input()))
print(collatzOutput)


while True:
    if collatzOutput == 1:
        print('ok')
        break
    else:
        collatz(int(input()))


