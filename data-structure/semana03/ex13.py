string = input("Digite algo: ")
nova = ""
for i in range(len(string)):
    if i + 3 <= len(string):
        tripla = string[i:i+3]
        c = 0
        if tripla not in string[:i+2]:
            print(f"{tripla}:", end=" ")
            for j in range(len(string)):
                if j + 3 <= len(string):
                    if string[j:j+3] == tripla:
                        c += 1
            print(c, end="   ")            
