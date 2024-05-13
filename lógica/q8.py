# 8. Dado um número inteiro positivo, escreva um programa que encontre o fatorial deste número.

number = int(input("Digite um número: "))

fatorial = 1

for i in range(1, number + 1):
    fatorial *= i

print(f"O fatorial de {number} é {fatorial}")