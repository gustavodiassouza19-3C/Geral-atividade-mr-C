#exercicios 4
tupla = (36.5, 37.2, 38.0, 36.8, 39.1)

for i in tupla:
    if 37.5 > i:
        print(f"{i}, normal")
    elif 38.5 > i and i > 37.5:
        print(f"{i}, Febre moderada")
    elif i>38.5:
        print(f"{i},Febre alta")