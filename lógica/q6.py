# 6. Dado uma lista de strings, escreva um programa que retorne uma lista com as strings ordenadas pelo seu tamanho.
lista_string = ['ddddd', 'fffffff', 'cccc', 'aa', 'eeeeee', 'bbb', 'gggggggg']

def ordenaPorTamanho(lista_string):
    return print(sorted(lista_string, key=len))

ordenaPorTamanho(lista_string)