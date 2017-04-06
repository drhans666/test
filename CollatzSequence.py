#Function detects if input number is even or odd, then adds Collatz sequence (even/2 ; 3 * odd + 1)
def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


#adds oportunity to enter number
print('Enter number:')
result = int(input())
print(result)

#loop checks if result is the end of sequence (1), if not result goes thru collatz function again
while True:
    if result == 1:
        print('End of Sequence')
        break
    else:
        result = collatz(result)
        print(result)


