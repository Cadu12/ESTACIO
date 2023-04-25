from tela import limparTela, imprimirTelaMenu, pressionarEnter

from adicionar import adicionar
from remover import remover
from atualizar import atualizar
from listar import listar

if __name__ == "__main__":
  while True:
    try:
      limparTela()
      imprimirTelaMenu()
      opcao = int(input("ESCOLHA A OPÇÃO: "))
      if opcao == 1:
        adicionar()
      elif opcao == 2:
        remover()
      elif opcao == 3:
        atualizar()
      elif opcao == 4:
        listar()
        pressionarEnter()
      elif opcao == 5:
        limparTela()
        print("SAIU COM SUCESSO.")
        break
    except:
      pass