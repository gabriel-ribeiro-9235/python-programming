string = input("Digite algo: ")
nova = ""
for i in range(len(string)):
    letra = string[i]
    c = 0
    for j in range(1, len(string)+1):
        if string[j-1] == letra and c == 0:
            c = j
    if c == len(string):
        nova += string[0]
    else:
        nova += string[c]
print(nova)
