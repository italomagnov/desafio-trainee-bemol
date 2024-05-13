# 5. Dado um número inteiro, escreva um programa para verificar se ele é um número primo.

number = int(input("Digite um número: "))

def isPrime(number):
    total = 0
    for i in range(1, number + 1):
        if number % i == 0:
            print('\033[33m', end = '')
            total += 1
        else:
            print('\033[31m', end = '')
        print(f'{i} ', end = '')

    print(f'\nO número {number} foi divisivel {total} vezes')
    if total == 2:
        print('E por isso ele é primo!')
    else:
        print('E por isso ele não é primo!')
        
isPrime(number)