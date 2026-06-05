class funcionario:
    def __init__(self,nome,matricula,salario_base):
        self.__nome=nome
        self.__matricula=matricula
        self.__salario_base=salario_base    

        #encapsulamento, usa o get para poder pegar o valor e retornar

    def get_nome(self):
        return(self.__nome)
        
    def get_matricula(self):
        return(self.__matricula)

    def get_salario_base(self):
        return(self.__salario_base)
        
    #set dos valores para nao haver erro do cadastro

    def set_nome(self, nome):
        if len(nome) > 0:
            self.__nome = nome
        else:
            print("erro o campo nome não pode abrigar um valor nulo")

    def set_salario_base(self, salario_base):
        if salario_base > 0:
            self.__salario_base = salario_base
        else:
            print("O salario não pode ser negativo cabra da peste")

    def set_matricula(self,matricula):
        if len(matricula) > 0:
            self.__matricula = matricula
        else:
            print("teu funcionario tem que ter cadastro")

    def exibir(self):
        print(f"Nome:{self.get_nome()}| Matricula: {self.get_matricula()}| Tipo: {self.get_tipo()}| Salario: {self.calcular_salario()}")


class CLT(funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)
        self.__tipo = "CLT"

    def set_tipo(self, tipo):
        if len(tipo) > 0:
            self.__tipo = tipo
        else:
            print("Fala teu tipo de contrato ne fiote")

    #polimorfismo calcular salario do profissional
    def calcular_salario(self,):
        return self.get_salario_base()
    
    def get_tipo(self):
        return (self.__tipo)
    
class gerente(funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)
        self.__tipo = "gerente"

    def set_tipo(self, tipo):
        if len(tipo) > 0:
            self.__tipo = tipo
        else:
            print("Fala teu tipo de contrato ne fiote")

    #polimorfismo calcular salario do profissional
    def calcular_salario(self):
        return self.get_salario_base() + 1500
    
    def get_tipo(self):
        return (self.__tipo)
    
class vendedor(funcionario):
    def __init__(self, nome, matricula, salario_base, vendas):
        super().__init__(nome, matricula, salario_base)
        self.__vendas = vendas
        self.__tipo = "vendedor"

    def set_vendas(self,vendas):
        if vendas >= 0:
            self.__vendas=vendas
        else:
            print("vendas nao podem ser negativas")

    def set_tipo(self, tipo):
        if 0 == len(tipo) :
            print("Fala teu tipo de contrato ne fiote")
        
    #polimorfismo calcular salario do profissional
    def calcular_salario(self):
        return self.get_salario_base() + self.__vendas * 0.1

    
    def get_tipo(self):
        return (self.__tipo)


trabalhadores=[
    CLT("gu", 1 , 1800),
    gerente("marco", 2, 2000),
    vendedor("paulo", 3, 3000, 100)
]

for i in trabalhadores:
    i.exibir()
