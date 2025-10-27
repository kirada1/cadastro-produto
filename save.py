import os
dict

class SalvarProdutos:
    def __init__(self, dados: dict[str, tuple[str, str, str]]) -> None:
        self.dados = dados

    def salvar_produto_criados(self) -> None:
        # primeiro verificar se o arquivo existe se não existir eu crio o arquivo
        if not os.path.exists("produtos.txt"):
            with open("produtos.txt", "w", encoding="utf8") as p:
                conteudo = p.write("")
                print(conteudo)
        # se o arquivo existir executa a função para salvar os dados
        else:
            with open("produtos.txt", "a+", encoding="utf8") as p:
                p.write(f"{self.dados}\n")
                p.seek(0)
                print(p.read())



