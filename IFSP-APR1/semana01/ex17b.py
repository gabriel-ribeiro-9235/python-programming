a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
t = a
if a > b:
    a = b
    b = t
    t = a
if a > c:
    a = c
    c = t
if b > c:
    t = b
    b = c
    c = t
print(f"A: {a}\nB: {b}\nC: {c}")
