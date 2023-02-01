import random

user_option = input('Elige Piedra, Papel o Tijera => ')
user_option = user_option.capitalize()

option = ['Piedra', 'Papel', 'Tijera']

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
    else:
        print("Papel gana a Piedra")
        print("Computer Gano")

elif user_option == "Papel":
    if computer_option == "Piedra":
        print("Papel gana a Piedra")
        print("User Gano!!")
    else:
        print("Tijera gana a Papel")
        print("Computer Gano")
elif user_option == "Tijera":
    if computer_option == "Papel":
        print("Tijera gana a Papel")
        print("User Gano!!")
    else:
        print("Piedra gana a Tijera")
        print("Computer Gano")
