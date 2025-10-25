from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os


class Produto:  # classe para criar o produto
    def __init__(self) -> None:
        self.produto: list[tuple[str, str, str]] = []
        self.fornecedores: list[str] = []
        self.fornecedorescomplete = WordCompleter(self.fornecedores, ignore_case=True)

    def CriarProduto(self) -> None:  # metodo para criar o produto
        while True:  # loop para inserir outros produtos, e tambem para validar a quantidade

            descricao = str(input("Descrição do produto: ")).strip()  # armazena descriçãpo
            fornecedor = prompt("fornecedor: ", completer=self.fornecedorescomplete)  # armazena o fornecedor
            familia = str(input("familia: ")).strip()

            juntar_tudo = (descricao, fornecedor, familia)
            self.produto.append(juntar_tudo)
            self.fornecedores.append(fornecedor)

            op = input("adicionar mais outro produto? S/N").lower().strip()
            if op != "s":
                break
            else:
                continue


class Menu(Produto):
    def __inir__(self) -> None:
        super().__init__()

    def Menus(self) -> None:  # metodo onde fica todos os menus
        #  menu principal
        self.MenuPrincipal = str(f"""{20*"="} M E N U {20*"="} 
            escolha uma opção valida
{49*"="}
[1] PRODUTOS
[2] ESTOQUE
[3] SAIR
""")
        #  segundo menu quando escolher a opção 1
        self.menuProduto = str(f"""{49*"="}
[1] ADICIONAR PRODUTO
[2] EDITAR PRODUTO
[3] EXCLUIR PRODUTO
[4] VOLTAR
""")
        #  segundo menu quando escolher a opçãp 2    
        self.MenueStoque = str(f"""{49*"="}
[1] SALDO EM ESTOQUE
[2] SALDO POR PRODUTO
[3] VOLTAR
""")

    # metodo para escolher as opções do menu
    def EscolherMenu(self) -> None:
        self.Menus()  # inicializando o metodo menu para utilizar os atributos dos menus
        while True:  # loop do primeiro menu
            os.system("clear")  # apaga o terminal antes de aparecer o menu para fica limpo

            print(self.MenuPrincipal)  # exibe o menu
            self.op = int(input(""))  # escolher a opção do menu

            # match case para controle das opções do menu
            match self.op:
                case 1:
                    while True:
                        os.system("clear")
                        print(self.menuProduto)

                        try:
                            op = int(input(" escolha uma opção: "))
                        except ValueError:
                            print("somente 1 2 ou 3")
                            continue

                        if op == 1:  # chama metodo de adicionar produto
                            self.CriarProduto()
                            continue
                        elif op == 2:  # chama metodo editar produto
                            pass  # obs metodo editar produto não criado ainda
                        else:  # se opção 3 volta para o menu anterior
                            break
                case 3:
                    print("progama finalizado ..............")
                    break
                case _:
                    print("opção errada.............")
