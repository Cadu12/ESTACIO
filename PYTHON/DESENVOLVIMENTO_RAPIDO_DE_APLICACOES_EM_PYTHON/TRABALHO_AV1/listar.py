from tela import limparTela


def listar():
  limparTela()
  print("┌──────────────────────────────────┬───────┐")
  print("│ NOME                             │ IDADE │")
  print("├──────────────────────────────────┼───────┤"),
  with open("dados", "r") as arquivo:
    for linha in arquivo.readlines():
      nome, idade = linha.split("\t")
      print("│ {:<32} │ {:<5} │".format(nome, idade.strip())),
  print("└──────────────────────────────────┴───────┘")
  print()
