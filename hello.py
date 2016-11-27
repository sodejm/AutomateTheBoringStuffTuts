# program says hello and asks for name.

print('Hello World!')
print('What is your name?') #asks for users name
myName = input()

print('It is good to meet you, ' + myName) # concat name
print('The length of your name is:')
print(len(myName)) # use len function for name length
print('What is your age?') # ask for user age
myAge = input()
print('You will be ' + str(int(myAge) +1) + ' in a year.') #not completely accurate but it works
