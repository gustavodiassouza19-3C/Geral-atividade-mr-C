class Pagamento:
    def processar(self, valor):
        return valor

class Dinheiro(Pagamento):
    def processar(self, valor):
        return valor * 0.95

class Cartao(Pagamento):
    def processar(self, valor):
        return valor * 1.02

class Pix(Pagamento):
    def processar(self, valor):
        return valor

formas_pagamento = [Dinheiro(), Cartao(), Pix()]
valor_original = 100.00

print(f"Valor original da compra: R$ {valor_original:.2f}\n")

for forma in formas_pagamento:
    nome_metodo = forma.__class__.__name__
    valor_final = forma.processar(valor_original)
    print(f"Pagamento em {nome_metodo}: R$ {valor_final:.2f}")