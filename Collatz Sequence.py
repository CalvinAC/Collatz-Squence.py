

print('Enter a number:')

def collatz(number):
##    print('DEBUG ' + str(number % 2))

    while number != 1:
        if number % 2 == 0:
            print(number//2)
            number = number // 2
        elif number % 2 == 1: 
            print(3 * number +1) 
            number = 3 * number + 1
try:
    collatz(int(input()))
except ValueError:
    print('You did not enter a number dummmy. The program will now self destruct.')

