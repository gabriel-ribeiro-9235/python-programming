nova = float(input("Informe a pressão desejada: "))
lida = float(input("Pressão lida: "))
if nova > lida:
    print(f"A diferença de pressão é {(nova - lida):.1f}, portanto o pneu será enchido.")
elif nova < lida:
    print(f"A diferença de pressão é -{(lida - nova):.1f}, portanto o pneu será esvaziado.")
else:
    print(f"A diferença de pressão é 0, seu pneu já está calibrado.")
