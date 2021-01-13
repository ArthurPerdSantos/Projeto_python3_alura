import random

def jogar():

    imprime_mensagem_abertura() # mostra a mensagem do jogo sendo jogado
    palavra_secreta = carrega_palavra_secreta() # carrega a palavra a ser usada na forca
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta) # carrega a estética das letras escolhidas

    erros = 0
    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not enforcou and not acertou):  # enquanto nao enforcou e nao acertou vai seguir em loop

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas, palavra_secreta)

        else:
            erros += 1
            desenha_forca(erros)


        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    elif (enforcou):
        imprime_mensagem_perdedor(palavra_secreta)

# imprime a mensagem de abertura
def imprime_mensagem_abertura():
    print("*************************************")
    print("Bem vindo ao jogo da forca!")
    print("*************************************")

# carrega a palavra a ser usada no jogo
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavra = []
    num_sec = 0
    for linha in arquivo:
        palavra.append(linha.strip())

    arquivo.close()

    num_sec = random.randrange(0, palavra.__len__())

    palavra_secreta = palavra[num_sec].upper()

    return palavra_secreta

# inicializa a estética do acerto de letras com _
def inicializa_letras_acertadas(palavra_secreta):
    lista = ["_" for letra in palavra_secreta] # preenche a lista com _ por razoes estéticas
    return lista

# identifica o chute do usuário
def pede_chute():
    chute = input("qual a letra escolhida?")
    chute = chute.strip().upper()
    return chute

# marca quando o chute é correto
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0

    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra

        index = index + 1


def desenha_forca(erros):
    print("  _____       ")
    print(" |/    |      ")


    if (erros == 1):
        print(" |    (_)     ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |    (_)     ")
        print(" |    \       ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |    (_)     ")
        print(" |    \|      ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |    (_)     ")
        print(" |    \|/     ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |    (_)     ")
        print(" |    \|/     ")
        print(" |    /       ")
        print(" |            ")

    if (erros == 6):
        print(" |    (_)     ")
        print(" |    \|/     ")
        print(" |     |      ")
        print(" |    /       ")
    if (erros == 7):
        print(" |    (_)     ")
        print(" |    \|/     ")
        print(" |     |      ")
        print(" |    / \     ")

    print(" |")
    print("_|___")


# imprime mensagem de vitória
def imprime_mensagem_vencedor():
    print("Voce Ganhou!!")
    print("Fim do jogo")

# imprime mensagem de derrota
def imprime_mensagem_perdedor(palavra):
    print("Voce Perdeu!!")
    print("A palavra secreta era {}".format(palavra))
    print("Fim do jogo")



if(__name__ == "__main__"):
    jogar()
