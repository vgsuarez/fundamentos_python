import random

option = ['Piedra', 'Papel', 'Tijera']

computer_wins = 0
user_wins = 0

rounds = 1

while True:

    print(' ')
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    print('COMPUTADORA ', computer_wins)
    print('USUARIO ', user_wins)
    print(' ')

    user_option = input('Elige Piedra, Papel o Tijera => ')
    user_option = user_option.capitalize()
    if not user_option in option:
        print('-' * 20)
        print('*' * 10)
        print('ELIJE UNA OPCION CORRECTA')
        print('*' * 10)
        print('-' * 20)
        continue
    rounds += 1

    computer_option = (random.choice(option))

    if computer_option == ("Piedra"):
        print("Computer elige Piedra")
    elif computer_option == ("Papel"):
        print("Computer elige Papel")
    else:
        print("Computer elige Tijera")

    if user_option == computer_option:
        print("Empate")

    elif user_option == "Piedra":
        if computer_option == "Tijera":
            print("Piedra gana a Tijera")
            print("User Gano!!")
            user_wins += 1
        else:
            print("Papel gana a Piedra")
            print("Computer Gano")
            computer_wins += 1

    elif user_option == "Papel":
        if computer_option == "Piedra":
            print("Papel gana a Piedra")
            print("User Gano!!")
            user_wins += 1
        else:
            print("Tijera gana a Papel")
            print("Computer Gano")
            computer_wins += 1

    elif user_option == "Tijera":
        if computer_option == "Papel":
            print("Tijera gana a Papel")
            print("User Gano!!")
            user_wins += 1
        else:
            print("Piedra gana a Tijera")
            print("Computer Gano")
            computer_wins += 1

    if computer_wins == 2:
        print('*' * 20)
        print('-' * 20)
        print('PERDISTE, LA COMPUTADORA GANO')
        print('-' * 20)
        print('*' * 20)
        break
    if user_wins == 2:
        print('*' * 20)
        print('-' * 20)
        print('VICTORIA!!!!, MUCHAS FELICIDADES')
        print('-' * 20)
        print('*' * 20)
        break
