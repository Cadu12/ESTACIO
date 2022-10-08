limite = 50
peso = float(input("Digite quantidade de KG's: "))
if peso > limite:
    print("Multa foi de R$", (peso - limite) * 4, "reais")