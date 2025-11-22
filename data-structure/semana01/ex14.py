print("Calculadora de Equação do segundo grau")
a = float(input("Insira o coeficiente a: "))
b = float(input("Insira o coeficiente b: "))
c = float(input("Insira o coeficiente c: "))
delta = b * b - 4 * a * c
if delta == 0:
    x = - b / (2 * a)
    print(f"Só há uma raiz real e ela vale {x}")
elif delta > 0:
    x1 = (- b + delta ** (1 / 2)) / (2 * a)
    x2 = (- b - delta ** (1 / 2)) / (2 * a)
    print(f"Há duas raízes reais e elas são {x1} e {x2}")
else:
    print("Delta é menor que zero, portanto não há raízes reais")
