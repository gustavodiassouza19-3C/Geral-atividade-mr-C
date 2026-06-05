class Sensor:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, valor):
        if -50 <= valor <= 150:
            self.__temperatura = valor
        else:
            print("Erro: Fora do limite físico")

    def status(self):
        if -50 <= self.__temperatura <= 80:
            return "Normal"
        elif 81 <= self.__temperatura <= 120:
            return "Alerta"
        else:
            return "Critico"

# Teste com 4 temperaturas
s = Sensor(25)

for temp in [50, 90, 130, 200]:
    s.set_temperatura(temp)
    print(f"Temp: {s.get_temperatura()} | Status: {s.status()}")