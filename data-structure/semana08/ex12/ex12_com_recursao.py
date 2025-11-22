def convBinario(num):
    if num == 0 or num == 1:
        return str(num)
    else:
        binario = convBinario(num//2) + str(num%2)
        return binario
    

n = int(input("Digite um número: "))
print(f"\"{n}\" em binário é \"{convBinario(n)}\"")
