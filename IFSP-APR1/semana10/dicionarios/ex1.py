def menu():
    print('''1. Adicionar Contato
2. Exibir Contatos
3. Excluir Contato
4. Alterar Contato
5. Sair''')
    n = int(input("Escolha uma opção: "))
    while n not in [1, 2, 3, 4, 5]:
        n = int(input("Escolha um opção válida: "))
    print('-'*40)
    return n


dic = {}
k = menu()
while k != 5:
    if k == 1:
        email = input("Email: ")
        if email in dic:
            print("Pessoa já cadastrada!")
        else:
            dic[email] = []
            dic[email].append(input('Nome: '))
            nasc = input("Data de nascimento (formato dd/mm/aaaa): ")
            while len(nasc) != 10 or nasc[2] != '/' or nasc[5] != '/':
                nasc = input("Data inválida! Tente novamente com a formatação correta (dd/mm/aaaa): ")
            dic[email].append(nasc)
            tuplas = []
            print('-'*40)
            print("Especialidades ".center(40))
            print('-'*40)
            esp = int(input("Quantas especialidades quer adicionar? "))
            for i in range(esp):
                print('-'*40)
                svc = input("Serviço: ")
                preco = float(input("Valor da hora: R$"))
                tupla = (svc, preco)
                tuplas.append(tupla)
            dic[email].append(tuplas)
        print('-'*40)
    elif k == 2:
        if dic != {}:
            for k, v in dic.items():
                print(f'Nome: {v[0]}')
                print(f'Email: {k}')
                print(f'Data de nascimento: {v[1]}')
                for tupla in v[2]:
                    print(f"Especialidade: {tupla[0]}")
                    print(f"\tValor da hora: R${tupla[1]:.2f}")
                print('-'*40)
        else:
            print("Ninguém foi cadastrado ainda!")
            print('-'*40)
    elif k == 3:
        if dic != {}:
            print('Contatos'.center(40))
            print('-'*40)
            for contato in dic:
                print(f'Email: {contato}\nNome: {dic[contato][0]}')
                print('-'*40)
            retirar = input("Digite o EMAIL do contato quer excluir: ") 
            while retirar not in dic:
                retirar = input("Não tem nenhum contato com o email inserido! Digite o EMAIL do contato que quer retirar: ")
            del dic[retirar]
        else:
            print("Ninguém foi cadastrado ainda!")
        print('-'*40)
    else:
        if dic != {}:
            print('Contatos'.center(40))
            print('-'*40)
            for contato in dic:
                print(f'Email: {contato}\nNome: {dic[contato][0]}')
                print('-'*40)
            atualizar = input("Digite o EMAIL do contato quer atualizar: ") 
            while atualizar not in dic:
                atualizar = input("Não tem nenhum contato com o email inserido! Digite o EMAIL do contato que quer atualizar: ")
            dic[atualizar] = []
            print('-'*40)
            dic[atualizar].append(input('Nome: '))
            nasc = input("Data de nascimento (formato dd/mm/aaaa): ")
            while len(nasc) != 10 or nasc[2] != '/' or nasc[5] != '/':
                nasc = input("Data inválida! Tente novamente com a formatação correta (dd/mm/aaaa): ")
            dic[atualizar].append(nasc)
            tuplas = []
            print('-'*40)
            print("Especialidades".center(40))
            print('-'*40)
            esp = int(input("Quantas especialidades quer adicionar? "))
            for i in range(esp):
                print('-'*40)
                svc = input("Serviço: ")
                preco = float(input("Valor da hora: R$"))
                tupla = (svc, preco)
                tuplas.append(tupla)
            dic[atualizar].append(tuplas)
        else:
            print("Ninguém foi cadastrado ainda!")
        print('-'*40)
    
    k = menu()
