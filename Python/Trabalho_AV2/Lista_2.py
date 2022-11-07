def soma_imposto(taxa_imposto, custo):
    return (1 + taxa_imposto / 100) * custo

custo = float(input("Digite o custo: "))
taxa = float(input("Digite a taxa de imposto: "))

print(f"Valor com imposto: {soma_imposto(taxa, custo):.2f}")
