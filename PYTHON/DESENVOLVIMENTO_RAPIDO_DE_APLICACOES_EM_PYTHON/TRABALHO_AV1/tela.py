import os


def limparTela():
  os.system("cls" if os.name == "nt" else "clear")


def imprimirTelaMenu():
  print("┌───────────────┐")
  print("│ 1 - ADICIONAR │")
  print("│ 2 - REMOVER   │")
  print("│ 3 - ATUALIZAR │")
  print("│ 4 - LISTA     │")
  print("│ 5 - SAIR      │")
  print("└───────────────┘")
  print()
  

def pressionarEnter():
  input("PRESSIONE ENTER PARA CONTINUAR.")
