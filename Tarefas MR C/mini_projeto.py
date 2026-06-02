class funcionario:
    def __init__(self,nome,matricula,salario_base):
        self._nome=nome
        self._matricula=matricula
        self._salario_base=salario_base
    
    def info_real(self):
        print(f"Nome:{self._nome}| Matricula: {self._matricula}| Tipo: {self._tipo}| Salario: {self._salario}")

class CLT(funcionario):
    def __init__(self, nome, matricula, salario_base, salario, tipo):
        self._salario=salario
        self._tipo=tipo
        super().__init__(nome, matricula, salario_base)
        


class vendedor(funcionario):
     def __init__(self, nome, matricula, salario_base, salario, tipo):
         self._salario=salario
         self._tipo=tipo
         super().__init__(nome,matricula,salario_base)



gustavo=CLT("gustavo", 1, 1500, 0, "CLT")

gustavo.info_real()