# CONDICIONALES
# if
'''
if True:
    print('deberia ejecutarse')

if False:
    print('nunca se ejecuta')
'''
# EJEMPLO NRO. 1
'''
pet = input('Cual es tu mascota favorita? ')
if pet == 'perro':
    print('genial tienes buen gusto')
if pet == gato:
    print('espero que tengas suerte')
'''
# EJEMPLO NRO. 2
'''
stock = int(input('Digita el stock => '))
if stock >= 100 and stock <= 1000:
    print('el stock es correcto')
else:
    print('el stock es incorrecto')
'''

# EJEMPLO NRO. 3
'''
pet = input('Cual es tu mascota favorita? ')

if pet == 'perro':
    print('genial tienes buen gusto')
elif pet == 'gato':
    print('espero que tengas suerte')
elif pet == 'pez':
    print('eres lo maximo')
else:
    print('que poco comun es tu mascota')
'''
# EJEMPLO NRO. 4
# IDENTIFICAR SI UN NUMERO ES PAR O IMPAR


'''
IDENTIFICAR SI UN NÚMERO ES PAR O IMPAR
'''

# Pide al usuario ingresar un número
number = int(input("Ingresa un número => "))

# Al número ingresado se realiza Operación Módulo entre 2
result = number % 2

# Si el resultado es 0 responde "ES PAR"
if(result == 0):
    print('ES PAR')

# Si el resultado es 1 responde "ES IMPAR"
else:
    print('ES IMPAR')
