def linha():
    print('-'*50)

    
def menu():
    print('''1. Incluir nova pessoa
2. Incluir novo telefone
3. Excluir telefone
4. Excluir pessoa
5. Consultar telefones
6. Sair''')
    n = int(input("Sua escolha: "))
    while n not in [1, 2, 3, 4, 5, 6]:
        n = int(input("Escolha inválida! Tente novamente: "))
    linha()
    return n


def incluirNovoNome(dic, name, lista):
    if name in dic:
        print(f"{name} já está na agenda!\nUse a opção 2 ou 3 para alterar os telefones dela.")
    else:
        dic[name] = lista
        print("Contato criado com sucesso!")
    linha()


def incluirTelefone(dic, name, tel):
    if name not in dic:
        resp = input(f"{name} não está na agenda, quer criar um novo contato? [S/N]").lower()
        while resp not in 'simnãonao':
            resp = input("Digite apenas \"S\" para \"sim\" e \"N\" para \"não\": ")
        if resp[0] == 's':
            incluirNovoNome(dic, name, [tel])
    else:
        dic[name].append(tel)
        print("Contato atualizado com sucesso!")
        linha()


def excluirTelefone(dic, tel):
    if dic == {}:
        print("Agenda vazia!")
    else:
        retirar = ()
        for chave in dic:
            for i in range(len(dic[chave])):
                if dic[chave][i] == tel:
                    retirar += (chave, i)
        if retirar == ():
            print(f"O telefone {tel} não está na sua agenda!")
        else:
            for i in range(0, len(retirar), 2):
                if len(dic[retirar[i]]) == 1:
                    del dic[retirar[i]]
                else:
                    del dic[retirar[i]][retirar[i+1]]
            print("Telefone excluído com sucesso!")
    linha()


def excluirNome(dic, name):
    if dic == {}:
        print("Agenda vazia!")
    else:
        if name not in dic:
            print(f"{name} não está na agenda!")
        else:
            del dic[name]
            print("Contato excluído com sucesso!")
    linha()
        

def consultarTelefone(dic, name):
    if dic == {}:
        print("Agenda vazia!")
    else:
        if name not in dic:
            print(f"{name} não está na agenda!")
        else:
            print(f"Telefone(s) de {name}".center(50))
            for i in range(len(dic[name])):
                linha()
                print(f"Telefone {i+1}: {dic[name][i]}")
    linha()


k = menu()
agenda = {}
while k != 6:
    if k == 1:
        nome = input("Nome do contato: ")
        num = int(input(f"Insira a quantidade de telefones de {nome}: "))
        while num <= 0:
            if num == 0:
                num = int(input("O contato deve ter pelo menos 1 telefone! Insira novamente a quantidade de telefones: "))
            else:
                num = int(input("Não pode ser um número negativo! Insira novamente a quantidade de telefones: "))
        telefones = []
        for i in range(num):
            telefones.append(input(f"Telefone {i+1}: "))
        incluirNovoNome(agenda, nome, telefones)
    elif k == 2:
        nome = input("Nome do contato: ")
        telefone = input("Novo telefone: ")
        incluirTelefone(agenda, nome, telefone)
    elif k == 3:
        telefone = input("Telefone que quer excluir: ")
        excluirTelefone(agenda, telefone)
    elif k == 4:
        nome = input("Nome do contato que quer excluir: ")
        excluirNome(agenda, nome)
    else:
        nome = input("Nome do contato que quer consultar: ")
        consultarTelefone(agenda, nome)
    k = menu()
