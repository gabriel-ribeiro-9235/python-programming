compra = float(input("Preço da compra: R$"))
if compra <= 100:
    desconto = 0.05
elif compra < 200:
    desconto = 0.1
else:
    desconto = 0.2
final = (1 - desconto) * compra
print(f"Comprando R${compra:.2f} você tem {desconto * 100:.0f}% de desconto.")
print(f"Preço final: R${final:.2f}")
