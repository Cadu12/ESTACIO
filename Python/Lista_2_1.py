print("Valor mínimo: R$ 10,00")
print("Valor máximo: R$ 600,00")
saque = int(input("Saque: R$ "))

while saque < 10 or saque > 600:
    print("Valor fora dos limites.")
    saque = int(input("Digite novamente: R$ "))

resto1 = saque % 100
resto2 = resto1 % 50
resto3 = resto2 % 10
resto4 = resto3 % 5
print("R$ 100,00:", saque // 100)
print("RR  50,00:", resto1 // 50)
print("R$  10,00:", resto2 // 10)
print("R$   5,00:", resto3 // 5)
print("R$   1,00:", resto4 // 1)