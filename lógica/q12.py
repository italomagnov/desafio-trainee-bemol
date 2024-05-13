# 12. Crie um programa que calcule o delta de uma equação do segundo grau (ax² + bx + c = 0)

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = (b**2) - (4*a*c)

print(f"O valor de delta é {delta}")