class animal:
    def __init__(self,nome,qnt_patas):
        self.nome=nome
        self.qnt_patas=qnt_patas

    def comer(self):
            print(f"{self.nome}, está comendo")

class cachorro(animal):
    def __init__(self,nome,qnt_patas):
        super().__init__(nome,qnt_patas)

    def latir(self):
        print("AuAU tigrão...")


marroni=cachorro("marroni",4)

marroni.comer()
