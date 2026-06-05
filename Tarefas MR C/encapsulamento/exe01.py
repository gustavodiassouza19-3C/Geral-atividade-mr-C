class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    # Getter para o nome
    def get_nome(self):
        return self.__nome

    # Setter para o nome
    def set_nome(self, nome):
        if len(nome.strip()) > 0:
            self.__nome = nome
        else:
            print("Erro: O nome do produto não pode ser vazio.")

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Erro: O preço do produto não pode ser negativo.")

prod = Produto("Teclado", 150.00)

print(f"Produto: {prod.get_nome()} | Preço: R$ {prod.get_preco():.2f}")

prod.set_preco(-25.00)

prod.set_preco(135.50)
print(f"Novo preço do {prod.get_nome()}: R$ {prod.get_preco():.2f}")