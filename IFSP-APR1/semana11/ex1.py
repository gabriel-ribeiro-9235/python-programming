def linha():
    print('-'*50)


def menu():
    print("""1- Adicionar aluno
2- Alterar aluno
3- Remover aluno
4- Consultar um aluno pela chave completa
5- Mostrar todos os alunos
6- Adicionar disciplina e notas ao aluno
7- Sair""")
    n = int(input("\nSua escolha: "))
    while n not in [1, 2, 3, 4, 5, 6, 7]:
        n = int(input("Escolha inválida! Tente novamente: "))
    linha()
    return n


def existe(dic, registro, alu):
    if (registro, alu) in dic:
        return True
    else:
        return False


def adicionaAluno(dic, dis):
    nome = input("Digite o nome do aluno: ")
    RA = input("Digite o RA do aluno: ")
    tem = existe(dic, RA, nome)
    if tem:
        print(f"{nome} já foi cadastrado!")
    else:
        data = input("Data de nascimento (DD/MM/AAAA): ")
        emails = []
        n = int(input(f"Quantos emails {nome} tem: "))
        for i in range(n):
            emails.append(input(f'Email {i+1}: '))
        notas = []
        for key in dis:
            disciplina = [dis[key][0]]
            disciplina.append(
                int(input(f"Digite a nota da disciplina {disciplina[0]}: ")))
            notas.append(disciplina)
        dic[(RA, nome)] = (data, emails, notas)
        print("Aluno cadastrado com sucesso!")
    linha()


def alteraAluno(dic, RA, nome):
    if existe(dic, RA, nome):
        print("""O que quer alterar?
1- Data de Nascimento
2- Emails
3- Notas""")
        n = int(input("Sua opção: "))
        while n not in [1, 2, 3]:
            n = int(input("Opção inválida! Tente novamente: "))
        if n == 1:
            linha()
            data = input("Digite a nova data (DD/MM/AAAA): ")
            dic[(RA, nome)] = data, + dic[(RA, nome)][1:]
            print("Data de nascimento alterada com sucesso!")
        elif n == 2:
            for i in range(len(dic[(RA, nome)][1])):
                print(f'{i+1} {dic[(RA, nome)][1][i]}')
            escolha = int(input(
                "Digite 1 para Trocar algum email, 2 para Adicionar um novo ou 3 para Excluir algum: "))
            while escolha not in [1, 2, 3]:
                escolha = int(
                    input("Escolha inválida! 1 para Trocar, 2 para Adicionar ou 3 para Excluir: "))
            if escolha == 1:
                troca = int(input(
                    f"Dos {len(dic[(RA, nome)][1])} emails listados acimas digite o número\n do que quer retirar:"))
                troca -= 1
                while not 0 <= troca < dic[(RA, nome)][1]:
                    troca = int(input("Escolha inválida! Tente novamente: "))
                    troca -= 1
                dic[(RA, nome)][1][troca] = input("Insira o novo email: ")
            elif escolha == 2:
                dic[(RA, nome)][1].append(input("Insira o novo email: "))
            else:
                exc = int(input(
                    f"Dos {len(dic[(RA, nome)][1])} emails listados acimas digite o número\n do que quer retirar:"))
                exc -= 1
                while not 0 <= exc < dic[(RA, nome)][1]:
                    exc = int(input("Escolha inválida! Tente novamente: "))
                    exc -= 1
                del dic[(RA, nome)][1][exc]
            print("Lista de emails alterada com sucesso!")
        else:
            for nota in dic[(RA, nome)][2]:
                print(f'{nota[0]}: {nota[1]}')
            escolha = input(
                "Digite o nome da matéria que você deseja alterar: ")
            esta = False
            for i in range(len(dic[(RA, nome)][2])):
                if dic[(RA, nome)][2][i][0] == escolha:
                    idx = i
                    esta = esta or True
            if esta:
                dic[(RA, nome)][2][idx][1] = float(
                    input(f"Digite a nova nota de {nome}: "))
                print("Lista do notas alteradas com sucesso!")
            else:
                print(f"Essa matéria não foi cadastrada nas notas de {nome}!")
    else:
        print(f"{nome} não foi cadastrado!")
    linha()


def removerAluno(dic, RA, nome):
    tem = existe(dic, RA, nome)
    if tem:
        del dic[(RA, nome)]
        print(f"{nome} removido!")
    else:
        print(f"{nome} não foi cadastrado!")


def consultarAlunoPelaChave(dic, chave):
    if chave not in dic:
        print(f"{chave[1]} não foi cadastrado!")
    else:
        print(f"Data de nascimento de {chave[1]}: {dic[chave][0]}")
        linha()
        print(f"Emails de {chave[1]}".center(50))
        linha()
        for email in dic[chave][1]:
            print(email)
        linha()
        print(f"Notas de {chave[1]}".center(50))
        for nota in dic[chave][2]:
            linha()
            print(f"Disciplina: {nota[0]}")
            print(f"Nota: {nota[1]}\n")
    linha()


def mostraTodosAlu(dic):
    if dic:
        for key, val in dic.items():
            print(f"Nome: {key[1]}")
            print(f"RA: {key[0]}")
            print(f"Data de nascimento: {val[0]}")
            linha()
            print("Emails".center(50))
            linha()
            for email in val[1]:
                print(email)
            linha()
            print("Notas".center(50))
            linha()
            for nota in val[2]:
                print(f"{nota[0]}: {nota[1]}")
    else:
        print("Nenhum aluno foi cadastrado!")
    linha()


def adicionarDiseNota(dic, dis):
    nome = input("Digite o nome da nova disciplina: ")
    sigla = input("Digite a sigla da disciplina: ")
    carga = float(input("Digite a carga horária da disciplina: "))
    dis[sigla] = [nome, carga]
    for key in dic:
        print(f"{key[1]} faz a disciplina?")
        print("""1- Sim
2- Não""")
        escolha = int(input("Opção: "))
        while escolha not in [1, 2]:
            escolha = int(input("Opção inválida! Tente novamente: "))
        if escolha == 1:
            linha()
            materia = [nome]
            materia.append(float(input(f"Digite a nota de {key[1]}: ")))
            dic[key][2].append(materia)
            print("Nota cadastrada com sucesso!")
        linha()


dic_alunos = {}
disciplinas = {}
k = menu()
while k != 7:
    if k == 1:
        adicionaAluno(dic_alunos, disciplinas)
    elif k == 2:
        aluno = input("Digite o nome do aluno: ")
        reg = input("Digite o RA do aluno: ")
        alteraAluno(dic_alunos, reg, aluno)
    elif k == 3:
        aluno = input("Digite o nome do aluno: ")
        reg = input("Digite o RA do aluno: ")
        removerAluno(dic_alunos, reg, aluno)
    elif k == 4:
        aluno = input("Digite o nome do aluno: ")
        reg = input("Digite o RA do aluno: ")
        consultarAlunoPelaChave(dic_alunos, (reg, aluno))
    elif k == 5:
        mostraTodosAlu(dic_alunos)
    else:
        adicionarDiseNota(dic_alunos, disciplinas)
    k = menu()
