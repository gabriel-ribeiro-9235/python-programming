dias = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']
temperaturas = list()
for dia in dias:
    temperaturas.append(float(input(f'Temperatura de {dia} (em °C): ')))
media = sum(temperaturas) / len(temperaturas)
cont = 0
for temp in temperaturas:
    if temp > media:
        cont += 1
print(f"Nessa semana, houve {cont} dias com temperatura maior que a média")
