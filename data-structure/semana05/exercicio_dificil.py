string = input("Digite algo: ")
nova = ""
for i in range(len(string)):
    c = 0
    for j in range(1, len(string)+1):
        if string[j-1] == string[i] and c == 0:
            c = j
    if c == len(string):
        nova += string[0]
    else:
        nova += string[c]
print(nova)


'''abacaxi
i = 0
string[i] = a
string[j-1] = string[0]
string[0] = string[i]
c = j = 1
string[c] = string[1]
string[1] = b
nova = bababia'''
