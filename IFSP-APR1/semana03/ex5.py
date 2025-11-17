string = input("Digite algo: ")
nova = string[0]
for i in range(len(string)):
    if i != 0:
        if string[i] != string[i-1]:
            nova += string[i]
print(nova)
