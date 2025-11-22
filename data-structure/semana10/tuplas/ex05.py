def tuplaStrings():
    n = int(input("Quantas strings você quer inserir? "))
    tupla = ()
    for i in range(n):
        elemento = input(f"{i+1}ª string: ")
        tupla += elemento,
        
    ttupla = ()
    for palavra in tupla:
    	ttupla += len(palavra),
    return ttupla


print(tuplaStrings())
