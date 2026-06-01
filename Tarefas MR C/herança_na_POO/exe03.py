class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir(self):
        print(f"Funcionário: {self.nome} | Salário Base: R$ {self.salario:.2f}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def salario_total(self):
        return self.salario + self.bonus

    def exibir(self):
        print(f"Gerente: {self.nome} | Salário Total: R$ {self.salario_total():.2f}")



func01 = Funcionario("Carlos Silva", 3000.00)
func01.exibir()

gerente01 = Gerente("Ana Souza", 6000.00, 2500.00)
gerente01.exibir()

total = gerente01.salario_total()


