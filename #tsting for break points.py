#tsting for break points 
while True:
    print('who are you?')
    name = input()
    if name != 'Happiness':
        continue
    print('Hello Happiness. what is the password? (it is a fish.)')
    password=input()
    if password=='jadezeus':
        break
print('thank you!')