import adivinhacao
import forca

while True:
    escolha = int(input("\n============================\n"
                        "||     Escolha o Jogo     ||\n"
                        "|| Adivinhação - Digite 1 ||\n"
                        "|| Forca       - Digite 2 ||\n"
                        "============================\n"
                        "Digite sua escolha: "))

    if escolha == 1:
        adivinhacao.jogar()
    elif escolha == 2:
        forca.jogar()
    else:
        print("Opção inválida, tente novamente!\n")

