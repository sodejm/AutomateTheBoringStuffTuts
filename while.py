while True:
    print('Who are you?')
    name = input()
    if name != 'Justin':
        continue
    print('Hellow, Justin. What is the password? (it is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access Granted')
