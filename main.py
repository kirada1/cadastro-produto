from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


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

    class Menu:
        def __inir__(self, op: int) -> None:
            self.op = op

        def EscolherMenu(self) -> None:
            print(f"""{20*"="} M E N U {20*"="}\n
{50*"="}\n
            [1]\n
            [2]\n
            [3]\n
            [4] """)
