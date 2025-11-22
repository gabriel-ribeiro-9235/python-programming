n = int(input("Digite um número: "))
soma = 0
while n < 0:
    n = int(input("Digite um número maior que 0: "))
n = str(n)
print(f"a) Centenas: {int(n)//100}")
print(f"Dezenas: {(int(n)%100)//10}")
print(f"Unidades: {int(n)%10}")
for digito in n:
    soma += int(digito)
print(f"\nb) Soma dos dígitos: {soma}")
print("\nc) O número é divisível por 3?", end=" ")
if int(n) % 3 == 0:
    print("Sim")
else:
    print("Não")
print("O número é divisível por 5?", end=" ")
if int(n) % 5 == 0:
    print("Sim")
else:
    print("Não")
if int(n) >= 100:
    print(f"\nd) Dígito das centenas: {(int(n)%1000)//100}")
    print(f"Dígito das unidade: {int(n)%10}")
else:
    print(f"\nd) Dígito das unidades: {int(n)%10}")
