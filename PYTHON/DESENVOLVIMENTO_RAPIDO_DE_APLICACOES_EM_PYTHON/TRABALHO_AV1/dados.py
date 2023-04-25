def isExiste(nome: str) -> bool:
  with open("dados", "r") as arquivo:
    for linha in arquivo.readlines():
      if linha.split("\t")[0] == nome.upper().strip():
        return True

  return False
