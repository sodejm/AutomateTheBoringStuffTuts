import sys
def collatz(num):
    if num % 2 == 0:
        print(num)
    if num % 2 == 1:
        print(3 * num + 1)

while True:
    try:
        print("Would you like to check a number?")
        try:
            number = int(input())
        except (NameError, ValueError) as e: # catching multiple errors in a line
            print("Please enter an integer")

        collatz(number)
    except KeyboardInterrupt:
        print('\nReceived interupt, exiting!')
        sys.exit() #somewhat graceful exit
