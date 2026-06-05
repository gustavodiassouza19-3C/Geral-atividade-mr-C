class Forma:
    def area(self):
        return 0

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

formas = [
    Triangulo(base=6, altura=4),
    Quadrado(lado=5),
    Triangulo(base=10, altura=5),
    Quadrado(lado=3)
]

for forma in formas:
    tipo_forma = forma.__class__.__name__
    print(f"Área do {tipo_forma}: {forma.area()}")