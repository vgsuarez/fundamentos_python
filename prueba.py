import random

option = ['Piedra', 'Papel', 'Tijera']

user_option = input('Elige Piedra, Papel o Tijera => ')
user_option = user_option.capitalize()
print('user option =>', user_option)

computer_option = (random.choice(option))
print('computer_option =>', computer_option)
