pesos = input("¿Qué cantidad de pesos desea cambiar a dolares?: ")
pesos = float(pesos)
valor_dolar = 42
dolares_convertidos = pesos / valor_dolar
dolares_convertidos = round(dolares_convertidos, 2)
dolares_convertidos = str(dolares_convertidos)
print("Tienes $" + dolares_convertidos + " dólares")