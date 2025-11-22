idade = int(input("Idade do eleitor: "))
if idade > 65:
    print(f"Com {idade} anos o voto é facultativo.")
elif idade >= 18:
    print(f"Com {idade} anos o voto é obrigatório.")
elif idade >= 16:
    print(f"Com {idade} anos o voto é facultativo.")
else:
    print(f"Com {idade} anos não se pode votar.")
