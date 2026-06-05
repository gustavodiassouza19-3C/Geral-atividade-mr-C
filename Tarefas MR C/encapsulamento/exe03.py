class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0.0   
        
    def get_saldo(self):
        return self.__saldo

    # Método para depositar
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

 
    def sacar(self, valor):
        if valor <= 0:
            print("Erro: O valor do saque deve ser positivo.")
        elif valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print(f"Erro: Saldo insuficiente para sacar R$ {valor:.2f}.")

   
    def extrato(self):
        print(f"--- EXTRATO ---")
        print(f"Titular: {self.__titular}")
        print(f"Saldo Atual: R$ {self.__saldo:.2f}")
        print("-" * 15)

 
conta = ContaBancaria("Ana Souza")

conta.extrato()
conta.depositar(500.00)
conta.sacar(200.00)
conta.sacar(400.00)  
conta.extrato()