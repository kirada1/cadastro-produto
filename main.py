from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os
from save import SalvarProdutos


class Produto:  # classe para criar o produto
    def __init__(self) -> None:
        self.produto: dict[str, tuple[str, str, str]] = {}
        self.fornecedores: list[str] = []
        self.fornecedorescomplete = WordCompleter(self.fornecedores, ignore_case=True)

    def CadastrarProduto(self) -> None:  # metodo para criar o produto
        while True:  # loop para inserir outros produtos, e tambem para validar a quantidade
            os.system("clear")
            descricao = str(input("Descrição do produto: ")).strip()  # armazena descriçãpo
            fornecedor = prompt("fornecedor: ", completer=self.fornecedorescomplete)  # armazena o fornecedor
            familia = str(input("familia: ")).strip()
            codigo_set = str(input("codigo set: ")).strip()

            produto_agrupado = (descricao, fornecedor, familia, )
            self.produto.update({codigo_set: produto_agrupado})

            op = input("adicionar mais outro produto? S/N").lower().strip()
            a = SalvarProdutos(self.produto)
            if op != "s":
                a.salvar_produto_criados()
                break
            else:
                a.salvar_produto_criados()
                continue


class Menu(Produto):
    def __inir__(self) -> None:
        super().__init__()

    # metodo onde fica todos os menus
    def Menus(self) -> None:
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
[1] CADASTRAR PRODUTO
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
                            self.CadastrarProduto()
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
