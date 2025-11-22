def perguntaTupla():
    n = int(input("Quantos números você quer inserir? "))
    tupla = ()
    for i in range(n):
        elemento = float(input(f"{i+1}º número: "))
        tupla += elemento,
    return tupla


print(perguntaTupla())
