nota = float(input("Nota: "))
while not(0 <= nota <= 100):
    nota = float(input("Nota inválida! Tente novamente: "))

if nota >= 86:
    print("Conceito A.")
elif nota >= 61:
    print("Conceito B.")
elif nota >= 36:
    print("Conceito C.")
elif nota > 0:
    print("Conceito D.")
else:
    print("Conceito E.")
