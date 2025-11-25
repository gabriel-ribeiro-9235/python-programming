def linha():
    print('-'*70)


# menu=======================================================
def menu():
    print('''1- Inserir produto
2- Efetuar venda
3- Exibir produtos abaixo do estoque mínimo
4- Alterar preço de produto
5- Sair''')
    k = int(input("Sua opção: "))
    while k not in [1, 2, 3, 4, 5]:
        k = int(input("Escolha inválida! Tente novamente"))
    linha()
    return k


# 1==========================================================
def insereProduto(dic):
    id = int(input("Insira o código do produto: "))
    if id in dic:
        print("O produto já foi inserido!")
    else:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Preço: R$"))
        quantidade = int(input("Quantidade no estoque: "))
        dic[id] = [nome, (preco, quantidade)]
    linha()


# 2==========================================================
def venda(dic, id, qnt):
    if id not in dic:
        return "Produto não encontrado"
    elif qnt > dic[id][1][1]:
        return "Impossível realizar a venda"
    else:
        preco = qnt*dic[id][1][0]
        dic[id] = [dic[id][0], (dic[id][1][0], dic[id][1][1]-qnt)]
        return f'Preço total da venda: R${preco:.2f}'


# 3==========================================================
def menorQue(dic, qnt):
    lista = []
    for key in dic:
        if dic[key][1][1] <= qnt:
            lista.append(dic[key][0])
    return lista


# 4==========================================================
def mudaPreco(dic, id, preco):
    if dic:
        if id not in dic:
            print("Produto não encontrado!")
        else:
            dic[id] = [dic[id][0], (preco, dic[id][1][1])]
            print("Preço alterado com sucesso!")
    else:
        print("Nenhum produto foi cadastrado ainda!")
    linha()


# 5==========================================================
def gravaArq(dic):
    import os
    if dic:
        if not os.path.exists("data-structure/semana12/produtos.txt"):
            arq = open("data-structure/semana12/produtos.txt", "x")
            arq.close
        arq = open("data-structure/semana12/produtos.txt", "w")
        for key in dic:
            arq.write(f"{key} \t {dic[key][0]} \t {dic[key][1]} \n")
            arq.close
    else:
        print("ERRO! Nenhum produto foi cadastrado ainda!")


# 6==========================================================
def leArq(arq):
    import os
    if os.path.exists(arq):
        dic = {}
        arquivo = open(arq, "r")
        for linha in arquivo:
            linha = linha[:-1]
            items = linha.split("\t")
            ID = int(items[0])
            nome = items[1]
            tupla = items[2].split(";")
            preco = float(tupla[0])
            qnt = int(tupla[1])
            dic[ID] = [nome, (preco, qnt)]
        arquivo.close()
        return dic
    else:
        print("ERRO! O arquivo produtos.txt não existe.")
        return "nada"
    

# 7==========================================================
def mostraFormatado(dic):
    for chave, valores in dic.items():
        print(f"""Código do produto: {chave}
Nome: {valores[0]}
Preço: R${valores[1][0]:.2f}
Quantidade: {valores[1][1]}""")
        linha()


produtos = leArq("data-structure/semana12/produtos.txt")
if produtos != "nada":
    n = menu()
else:
    n = 5

while n != 5:
    if n == 1:
        insereProduto(produtos)
    elif n == 2:
        if produtos:
            cd = int(input("Digite o código do produto: "))
            quantidade = int(input("Digite quantas unidades vai vender: "))
            linha()
            print(venda(produtos, cd, quantidade))
        else:
            print("Nenhum produto foi cadastrado ainda!")
        linha()
    elif n == 3:
        if produtos:
            quantidade = int(input("Digite a quantidade mínima que você quer verficar: "))
            menos_min = menorQue(produtos, quantidade)
            linha()
            print(f"No estoque tem os seguintes produtos com {quantidade} ou menos unidades:\n")
            if menos_min == []:
                print("Nenhum produto encontrado")
            else:
                for item in menos_min:
                    print(item)
        else:
            print("Nenhum produto foi cadastrado ainda!")
        linha()
    elif n == 4:
        if produtos:
            reg = int(input("Insira o código do produto que você quer mudar o preço: "))
            novo = float(input("Novo preço: R$"))
            mudaPreco(produtos, reg, novo)
        else:
            print("Nenhum produto foi cadastrado ainda!") 
            linha()           
    n = menu()
if produtos != "nada":
    gravaArq(produtos)

print(produtos)
