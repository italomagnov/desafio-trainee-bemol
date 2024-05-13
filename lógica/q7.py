# 7. Dada uma string, escreva um programa que retorne à primeira letra que não se repete.
string = input("Digite uma frase ou uma palavra: ")

for i in string:
    if string.count(i) == 1:
        print(i)
        break