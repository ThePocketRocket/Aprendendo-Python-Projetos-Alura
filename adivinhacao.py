import random
import time


def jogar():
    print("Jogo de adivinhação!")

    rodada = 1
    nivel = 0
    tentativas = 0
    pontos_de_vida = 0
    numero = random.randint(1, 100)

    while True:
        nivel = int(input("Digite o nível de dificuldade!\n"
                          "Fácil   - Digite 1\n"
                          "Médio   - Digite 2\n"
                          "Difícil - Digite 3\n"
                          "Escolha seu nível: "))

        if nivel == 1:
            tentativas = 15
            pontos_de_vida = 1500
            break
        elif nivel == 2:
            tentativas = 10
            pontos_de_vida = 1000
            break
        elif nivel == 3:
            tentativas = 5
            pontos_de_vida = 500
            break
        else:
            print("\nVocê não digitou uma opção válida!")

    for rodada in range(1, tentativas + 1):
        print("\n\nTentativa {} de {}".format(rodada, tentativas))

        while True:
            chute = int(input("Digite um número entre 1 e 100: "))
            acertou = numero == chute

            if chute < 1 or chute > 100:
                print("Você digitou um número fora do intervalo!\n"
                      "Tente novamente!\n")
                continue
            else:
                break

        if acertou:
            print("Você Ganhou! E permaneceu com {} pontos de vida ❤️".format(pontos_de_vida))
            break
        else:
            pontos_de_vida -= 100
            chute_alto = chute > numero
            if chute_alto:
                print("Chutou alto!\n")
            else:
                print("Chutou baixo!\n")

            if pontos_de_vida == 0:
                print("Você Perdeu! Seus pontos de vida zeraram! 💔")
                break

    print("Fim de Jogo")
    time.sleep(3)
