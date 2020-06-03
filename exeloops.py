from random import choice

nomes = []

for i in range (8):
    nome = input("Escreve o nome de 8 dos teus amigos: ")
    nomes.append(nome) # adiciona os nomes à lista

nome_escolhido = choice(nomes)# escolhe um nome aleatoriament da lista
print(nome_escolhido)
    
             
