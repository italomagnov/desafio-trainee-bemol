# 9. Crie um minijogo “adivinhe o número”, o jogador terá que adivinhar qual é o número coringa (37)
# Ele pode ter 5 tentativas, se acertar (aqui entende-se acertar se o jogador inserir o número 37), revele o número
# Caso exceda, imprima na tela “Game Over”. 
# Informar na tela que o número oculto é entre 0 e 100.

print("=-=-=-=-=- ADVINHE O NUMERO -=-=-=-=-=")
# resposta = input(">>>>> Pressione 1 para iniciar ou 2 para sair <<<<<\n")

def discover_number():
    joker_number = 37
    attempts = 5
    
    print("O numero oculto é entre 0 e 100")
        
    while attempts > 0:
        print(f"Você tem {attempts } tentativas restantes")
        guess = int(input("Digite sua resposta: "))
        
        if guess == joker_number:
            print(f"Parabéns, você acertou!!! O número coringa era {joker_number}")
            return
        else:
            print("hmmm resposta errada :/ Tente de novo")
            attempts -= 1
       
    print("Game Over")
        
while True:
    resposta = int(input(">>>>> Pressione 1 para iniciar ou 2 para sair <<<<<\n"))
    
    if resposta == 1:
        discover_number()
    elif resposta == 2:
        print("Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")