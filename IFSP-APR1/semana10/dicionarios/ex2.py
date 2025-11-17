def menu():
    print(f'''1. Cadastrar aluno
2. Ver alunos cadastrados
3. Excluir aluno
4. Sair''')
    n = int(input("Sua Escolha: "))
    while n not in [1, 2, 3, 4]:
        n = int(input("Escolha inválida! Tente novamente: "))
    print('-'*50)
    return n


dic = {}
k = menu()
while k != 4:
    if dic == {} and k in [2, 3]:
        print("Nenhum aluno foi cadastrado!")
        print('-'*50)
    else:
        if k == 1:
            nome = input("Nome do aluno: ")
            RA = input("RA do aluno: ")
            data = input("Data de nascimento (dd/mm/aaaa): ")
            while len(data) != 10 or data[2] != '/' or data[5] != '/':
                data = input("Data inválida! Digite no formato dd/mm/aaaa: ")
            n_emails = int(input("Número de emails do aluno: "))
            while n_emails < 0:
                n_emails = int(inptu("Não pode ser negativo! Tente novamente: "))
            emails = []
            for i in range(n_emails):
                print('-'*50)
                emails.append(input(f"Email {i+1}: "))
            print('-'*50)
            n_tel = int(input("Quantidade de telefones do alunos: "))
            while n_tel < 0:
                n_tel = int(input("Não pode ser negativo! Tente novamente: "))
            tels = []
            for i in range(n_tel):
                print('-'*50)
                tels.append(input(f"Telefone {i+1}: "))
            dic[(RA, nome)] = (data, emails, tels)
            print('-'*50)
        elif k == 2:
            for chave in dic:
                print(f"Nome: {chave[1]}")
                print(f"RA: {chave[0]}")
                print(f"Data de nascimentos: {dic[chave][0]}")
                print("Emails:")
                for email in dic[chave][1]:
                    print(email)
                print("Telefones:")
                for tel in dic[chave][2]:
                    print(tel)
                print('-'*50)
        else:
            print("Alunos cadastrados".center(50))
            print('-'*50)
            for chave in dic:
                print(f"Nome: {chave[1]}")
                print(f"RA: {chave[0]}")
                print('-'*50)
            retira_nome = input("Nome do aluno que quer retirar: ")
            retira_RA = input("RA do aluno que quer retirar: ")
            retira = (retira_RA, retira_nome)
            print('-'*50)
            if retira in dic:
                print(f"Aluno {retira[1]} excluído com sucesso!")                    
                del dic[retira]
            else:
                print(f"Nenhum aluno foi cadastrado com nome {retira[1]} e RA {retira[0]}!")
            print('-'*50)
    k = menu()
