class Instrumento:
    def tocar(self):
        print("Som genérico de instrumento.")

class Violao(Instrumento):
    def tocar(self):
        print("Som de violão vrau!")

class Bateria(Instrumento):
    def tocar(self):
        print("Som de bateria kabum")

class Piano(Instrumento):
    def tocar(self):
        print("Som de piano katchau!")

instrumentos = [Violao(), Bateria(), Piano()]

for instrumento in instrumentos:
    instrumento.tocar()