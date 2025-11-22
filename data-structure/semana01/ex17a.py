from statistics import median
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
lista = [a, b, c]
a = min(lista)
b = median(lista)
c = max(lista)
print(f"A: {a}\nB: {b}\nC: {c}")
