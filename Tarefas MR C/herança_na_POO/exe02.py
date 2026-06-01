class veiculo:
    def __init__ (self,marca, ano):
        self.marca=marca
        self.ano=ano

    def info(self):
        print(f"{self.marca} e o ano é {self.ano}")

class moto(veiculo):
    def __init__ (self,marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

class carro(veiculo):
    def __init__(self, marca, ano, portas):
        
        super().__init__(marca, ano)
        self.portas = portas


moto_eletro=moto("eletrica", 1990, "50pm")

bmw=carro("caminhonete", 2000, "4")

bmw.info()
moto_eletro.info()