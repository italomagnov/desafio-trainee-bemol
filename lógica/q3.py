# 3. Escreva um programa que receba uma string e retorne a mesma string, mas com as vogais removidas.
def removeVogais():
    string = input('Digite uma frase ou uma palavra: ')
    print(string.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', ''))
    
removeVogais()