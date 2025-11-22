alfabeto = "abcdefghijklmnopqrstuvwxyz"
string = input("Digite algo: ")
nova = ""
for i in range(len(string)):
    c = 0
    for j in range(1, len(alfabeto)+1):
        if string[i] == alfabeto[j-1]:
            c = j
    if c != 0:
        nova += alfabeto[-c]
print(nova)
