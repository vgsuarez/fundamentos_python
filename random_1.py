import random

option = ['1', '2', '3']

computer_option = (random.choice(option))

if computer_option == '1':
    print('Piedra')
elif computer_option == '2':
    print('Papel')
else:
    print('Tijera')
