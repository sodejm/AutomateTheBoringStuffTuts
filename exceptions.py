def spam(divideBy):
    # add the try catch
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(spam(2))
print(spam(12))
print(spam(0)) # can't divide by zero
print(spam(1))
