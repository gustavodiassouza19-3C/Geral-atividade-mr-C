class pessoas:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade(idade)
        
    def set_nome(self,nome):
        if len(nome) >= 0:
            self.__nome = nome
        else:
            print("O valor nao pode ser vazio")
        
    def set_iade(self,idade):
        if idade > -1 or 121 > idade:
            self.__idade = idade
        else:
            print("Idade invalida")
            
    def apresentar(self):
        print()