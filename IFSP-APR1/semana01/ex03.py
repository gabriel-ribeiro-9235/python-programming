nome = str(input("Informe o nome do aluno: ")).strip()

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2

print(f"A média das notas de {nome} é {media:.1f}.")
