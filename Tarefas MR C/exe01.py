class Aluno:
    def __init__(self, nome, nota):
        self.__nome = nome
        self.__nota = nota

    def get_nome(self):
        return self.__nome
        
    def get_nota(self):
        return self.__nota
    
    def set_nome(self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            print("ERRO")
    
aluno1 = Aluno("ana", 90)
print(aluno1.get_nome())
