t1 = int(input("Informe o número de tomadas da primeira régua: "))
t2 = int(input("Informe o número de tomadas da segunda régua: "))
t3 = int(input("Informe o número de tomadas da terceira régua: "))
t4 = int(input("Informe o número de tomadas da quarta régua: "))
total = t1 + (t2 - 1) + (t3 - 1) + (t4 - 1)

print(f"Com as réguas dadas é possível usar um número máximo de {total} tomadas")
