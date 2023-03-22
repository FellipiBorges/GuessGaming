print("***********************")
print("Bem vindo ao jogo da adivinhação!")
print("***********************")

numero_secreto = 42

chute = input("Digite o seu numero: ")

chute = int(chute)

print("Você digitou " , chute)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você erroooou!")

print("Fim de Jogo")