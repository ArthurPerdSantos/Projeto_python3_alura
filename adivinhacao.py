
import random
def jogar():
    print("*************************************")
    print("Bem vindo ao jogo da adivinhação!")
    print("*************************************")

    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("1 - fácil   2 - Médio    3 - Difícil")

    nivel = int(input("define o nível: "))


    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

        numero_secreto = random.randrange(1, 101)  # numero aleatorio entre 1 e 100

    for rodada in range (1, tentativas + 1): # for faz nesse modelo, podendo por(1, tentativas +1, 2(esse definindo a quantidade somada no count do for))

        print(f"Tentativa {rodada} de {tentativas}")#método de print usando de var já criadas
        #print("Tentativa {} de {}".format(rodada,tentativas)) possivel fazer assim tbm
        chute = int(input("digite um numero entre 1 e 100: "))#input sempre é string quando recebe, o int() serve para converter para inteiro
        print("voce digitou", chute)
        if(chute < 1 or chute > 100):# or é igual a ||
            print("voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos))
            break

        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(menor):#basicamente um else if
                print("Você errou! O seu chute foi menor que o número secreto.")
            if(rodada == tentativas):
                print("Você não acertou no número max de tentativas. Esse era o numero secreto: {}, você fez {} pontos".format(numero_secreto, pontos))
            pontos_perdidos = numero_secreto - chute
            pontos -= abs(pontos_perdidos)

    print("fim do jogo")

if(__name__ == "__main__"):
    jogar()