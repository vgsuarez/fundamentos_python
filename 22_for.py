# imprime una lista numeros de un rango establecido
'''
for element in range(0, 11):
    print(element)

#Si solo un dato es este caso 20 se imprime del 0 al 19
for element in range(20):
    print(element)
'''
'''
my_list = [32, 45, 67, 89, 43]
for element in my_list:
    print(element)

my_tuple = ('nico', 'julio', 'santi')
for element in my_tuple:
    print(element)
'''
'''
product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}
'''
# for key in product:
#     print(key, '=>', product[key])
'''
for key, value in product.items():
    print(key, '=>', value)
'''
'''
people = [
    {
        'name': 'nico',
        'edad': 25
    },
    {
        'name': 'julia',
        'edad': 30
    },
    {
        'name': 'lucas',
        'edad': 13
    }
]
for person in people:   
    print('name =>', person['name'])
'''
'''
primos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primos[3:10:2]

city = 'casa'
print(city)
'''

city = 'NY'
if city == 'NY':
    print('Welcome to new york city')
