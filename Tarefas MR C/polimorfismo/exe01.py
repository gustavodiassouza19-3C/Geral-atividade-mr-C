class Funcionario:
    def calcular_salario(self):
        return 0

class Vendedor(Funcionario):
    def __init__(self, salario_fixo, comissao):
        self.salario_fixo = salario_fixo
        self.comissao = comissao

    def calcular_salario(self):
        # Sobrescreve o método: salário fixo + comissão
        return self.salario_fixo + self.comissao

class Gerente(Funcionario):
    def __init__(self, salario_fixo, bonus):
        self.salario_fixo = salario_fixo
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_fixo + self.bonus

vendedor = Vendedor(salario_fixo=2500.00, comissao=600.00)
gerente = Gerente(salario_fixo=6000.00, bonus=1500.00)

print(f"Salario vendedor: R$ {vendedor.calcular_salario()}")
print(f"salario Gerente: R$ {gerente.calcular_salario()}")