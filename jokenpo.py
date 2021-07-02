import random

print("JOGO PEDRA PAPEL E TESOURA \nOpções:\n0-Pedra \n1-Papel\n2-Tesoura")

opcoes = ['pedra', 'papel', 'tesoura']

jogada_computador = random.choice(opcoes)

jogadaUsuario=int(input("Digite a sua jogada: "))

if jogada_computador == "pedra":
    print("O computador escolheu: Pedra")
    if jogadaUsuario == 0:
        print("Empatou!")
    elif jogadaUsuario == 1:
        print("Uhull!! Você ganhou!")
    elif jogadaUsuario == 2:
        print("Você perdeu!")
    else:
        print("Número invalido")

elif jogada_computador == "papel":
    print("O computador escolheu: Papel")
    if jogadaUsuario == 0:
        print("Você perdeu!")
    elif jogadaUsuario == 1:
        print("Empate!")
    elif jogadaUsuario == 2:
        print("Uhull!! Você ganhou!")
    else:
        print("Número invalido")
        
elif jogada_computador == "tesoura":
    print("O computador escolheu: Tesoura")
    if jogadaUsuario == 0:
        print("Uhull!! Você ganhou!")
    elif jogadaUsuario == 1:
        print("Você perdeu!")
    elif jogadaUsuario == 2:
        print("Empate!")
    else:
        print("Número invalido")
else:
    print("Número invalido")



