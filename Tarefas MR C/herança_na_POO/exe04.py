class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.latitude = idade 
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(f"[ALUNO] Nome: {self.nome} | Idade: {self.idade} | Matrícula: {self.matricula}")

class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print(f"[PROFESSOR] Nome: {self.nome} | Idade: {self.idade} | Salário: R$ {self.salario}")

comunidade_escolar = [
    Aluno("Lucas", 16, "2026XYZ"),
    Professor("Diego", 35, 4500.00),
    Aluno("Mariana", 17, "2026ABC")
]

for pessoa in comunidade_escolar:
    pessoa.apresentar()
