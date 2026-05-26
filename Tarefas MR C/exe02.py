class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco(preco)

  
    

    def set_nome(self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            print("Erro: O nome não pode ser vazio.")

    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Erro: O preço não pode ser negativo.")
            self.__preco = 0  


produto1 = Produto("Batata", 100)
produto2 = Produto("Banana", 6769)

print(produto1.get_nome())
print(produto2.get_preco())


produto1.set_preco(-50)  
print(produto1.get_preco())  
