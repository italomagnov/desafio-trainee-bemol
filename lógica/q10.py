# 10. Crie um programa que receba 10 números e ordene em ordem crescente.

numeros = []

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

numeros_ordenados = sorted(numeros)
print("Números em ordem crescente:", numeros_ordenados)
