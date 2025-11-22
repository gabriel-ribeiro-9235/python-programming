livros = int(input("Quantidade de livros que quer comprar: "))
a = livros * 0.25 + 7.5
b = livros * 0.5 + 2.5
print(f"Pelo critério A você pagará R${a:.2f}.")
print(f"Pelo critério B você pagará R${b:.2f}.")
if a < b:
    print("É mais vantajoso comprar pelo critério A.")
elif b < a:
    print("É mais vantajoso comprar pelo critério B.")
else:
    print("Você vai pagar a mesma coisa escolhendo o critério B ou A")
