

spam = ['apples', 'bananas', 'tofu', 'cats']

def printit(listvar):
    print(listvar[0], end=' ')
    for i in range(1, len(listvar)):
        print('and ' + listvar[i], end=' ')
        if i == len(listvar) - 1:
            print('\n')

printit(spam)
