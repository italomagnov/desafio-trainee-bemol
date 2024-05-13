# 1. Crie um programa que receba duas idades inteiras e imprima na tela a maior idade.
def maiorIdade():
    idade1 = int(input("Digite a primeira idade: "))
    idade2 = int(input("Digite a segunda idade: "))
    
    if idade1 > idade2:
        print(f"Maior idade: {idade1}")
    else:
        print(f"Maior idade: {idade2}")
        
maiorIdade()