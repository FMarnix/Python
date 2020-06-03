import random

cores = ["azul", "vermelho", "verde", "amarelo", "preto", "rosa", "laranja"]

while True:
    cor = cores[random.randint(0, len(cores)-1)]
    guess = input("Estou a pensar numa cor, consegues adivinhar qual é?: ")

    while True:
        if(cor == guess.lower()):
            break
        else:
            guess = input("Não. Tenta outra vez: ")

    print("Adivinhaste! Eu estava a pensar", cor)

    play_again = input("Vamos jogar outra vez? Diz 'não' para parar")

    if play_again.lower() == 'no':
        break

print("Foi divertido, obrigado por jogares")
