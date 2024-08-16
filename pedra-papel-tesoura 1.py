import random
import time

# Função para o desenho da mão referente ao Papel
def papel():
    return """
        Papel
        _______
    ---'   ____)
            ______)
            _______)
            _______)
    ---.__________)
    """

# Função para o desenho da mão referente à Pedra
def pedra():
    return """
        Pedra
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """

# Função para o desenho da mão referente à Tesoura
def tesoura():
    return """
        Tesoura
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """

# Opções possíveis e suas respectivas funções
opcoes = {"pedra": pedra, "papel": papel, "tesoura": tesoura}

# Função para realizar uma rodada do jogo
def jogar_rodada():

    # Usado para converter as letras em minúsculas caso o usuário as coloque maiúsculas
    escolha_usuario = input("Escolha entre pedra, papel e tesoura: ").lower()

    # Simula o momento antes das escolhas, característico do jogo
    print('JO')
    time.sleep(1)  # Pausa de 1 segundo
    print("KEN")
    time.sleep(1)  # Pausa de 1 segundo
    print("PÔ!\n")
    time.sleep(0.5)  # Pausa de meio segundo

    # Verifica se a escolha do usuário é válida
    if escolha_usuario not in opcoes:
        print("Escolha inválida. Tente novamente.")
        return None  # Retorna None para indicar escolha inválida

    # Escolhe aleatoriamente uma opção para o computador
    escolha_computador = random.choice(list(opcoes.keys()))

    # Exibe a escolha do usuário
    print("Sua escolha:")
    print(opcoes[escolha_usuario]())

    # Exibe a escolha do computador
    print("Escolha do adversário:")
    print(opcoes[escolha_computador]())

    # Verifica o resultado da rodada
    if escolha_usuario == escolha_computador:
        print("É um empate!")
        return "empate"  # Retorna "empate" se as escolhas forem iguais
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        print("Você ganhou!")
        return "usuario"  # Retorna "usuario" se o usuário vencer
    else:
        print("O adversário ganhou!")
        return "computador"  # Retorna "computador" se o computador vencer

# Função para realizar o o jogo no formato "melhor de 3".
def melhor_de_3():

    # Variáveis para armazenar as vitórias do usuário e do computador
    vitorias_usuario = 0
    vitorias_computador = 0

    # Continua jogando até que um dos jogadores vença 2 rodadas
    while vitorias_usuario < 2 and vitorias_computador < 2:
        resultado = jogar_rodada()  # Realiza uma rodada

        # Atualiza o placar com base no resultado
        if resultado == "usuario":
            vitorias_usuario += 1

        elif resultado == "computador":
            vitorias_computador += 1

        # Exibe o placar atual
        print("\nPlacar: Você {} - {} Adversário\n".format(vitorias_usuario, vitorias_computador))

    # Verifica o vencedor do jogo
    if vitorias_usuario == 2:
        print("Parabéns! Você venceu o jogo!")
    else:
        print("O adversário venceu o jogo!")

# Inicia o jogo
melhor_de_3()
