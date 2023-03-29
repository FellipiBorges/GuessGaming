print("***********************")
print("Bem vindo ao jogo da adivinhação!")
print("***********************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativas {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite um número entre 1 e 100: ")
    chute = int(chute)
    print("Você digitou " , chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou =   chute == numero_secreto
    maior =     chute > numero_secreto
    menor =     chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você erroooou! Seu chute foi maior que o número secreto")
        if(menor):
            print("Você erroooou! Seu chute foi menor que o número secreto")


print("Fim de Jogo")