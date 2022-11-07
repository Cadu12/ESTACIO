sexo = int(input("Digite seu sexo:\n - [1] Para homem\n - [2] Para mulher\nEscolha uma opção: "))
altura = float(input("Digite sua altura: "))
if sexo == 1:
    print("Seu peso ideal é", (72.7 * altura) - 58, "quilos")
elif sexo == 2:
    print("Seu peso ideal é", (62.1 * altura) - 44.7, "quilos")