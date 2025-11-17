p = int(input("Digite a posição da porta P [0/1]: "))
while p != 0 and p != 1:
    p = int(input("Posição inválida! Digite a posição da porta P [0/1]: "))
r = int(input("Digite a posição da porta R [0/1]: "))
while r != 0 and r != 1:
    r = int(input("Posição inválida! Digite a posição da porta R [0/1]: "))
if p == 0:
    print("A bolinha seguiu o caminho C.")
else:
    if r == 0:
        print("A bolinha seguiu o caminho B")
    else:
        print("A bolinha seguiu o caminho A")
