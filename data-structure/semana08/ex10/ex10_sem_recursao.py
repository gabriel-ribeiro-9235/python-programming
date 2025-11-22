string = input("Digite algo: ")
sbstring = input("Digite uma substring: ")
cont = 0
if len(sbstring) > len(string):
    print("Substring maior que a string!")
else:
    for i in range(len(string)):
        if i + len(sbstring) <= len(string) and string[i:i+len(sbstring)] == sbstring:
            cont += 1
print(f"{sbstring} aparece {cont} vezes na {string}")
