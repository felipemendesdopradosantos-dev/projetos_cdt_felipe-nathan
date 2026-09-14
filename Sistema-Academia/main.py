import banco
import frequencia


def cadastrar():
    print("\n========== CADASTRO DE ALUNO ==========")

    nome = input("Nome: ")

    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida.")
        return

    telefone = input("Telefone: ")
    email = input("E-mail: ")
    plano = input("Plano: ")

    try:
        valor_plano = float(
            input("Valor do plano: R$ ").replace(",", ".")
        )
    except ValueError:
        print("Valor inválido.")
        return

    banco.cadastrar_aluno(
        nome,
        idade,
        telefone,
        email,
        plano,
        valor_plano
    )

    print("\nAluno cadastrado com sucesso!")


def listar():
    print("\n========== ALUNOS CADASTRADOS ==========")

    alunos = banco.listar_alunos()

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print(f"""
Matrícula: {aluno[0]}
Nome: {aluno[1]}
Idade: {aluno[2]}
Telefone: {aluno[3]}
E-mail: {aluno[4]}
Plano: {aluno[5]}
Valor: R$ {aluno[6]:.2f}
Status: {aluno[7]}
------------------------------------------
""")


def buscar():
    print("\n========== BUSCAR ALUNO ==========")

    try:
        id_aluno = int(input("Digite a matrícula do aluno: "))
    except ValueError:
        print("Matrícula inválida.")
        return

    aluno = banco.buscar_aluno(id_aluno)

    if aluno is None:
        print("\nAluno não encontrado.")
        return

    print(f"""
Aluno encontrado!

Matrícula: {aluno[0]}
Nome: {aluno[1]}
Idade: {aluno[2]}
Telefone: {aluno[3]}
E-mail: {aluno[4]}
Plano: {aluno[5]}
Valor: R$ {aluno[6]:.2f}
Status: {aluno[7]}
""")


def menu():
    while True:
        print("""
========================================
       SISTEMA DE ACADEMIA
========================================

1 - Cadastrar aluno
2 - Listar alunos
3 - Buscar aluno
4 - Editar aluno
5 - Excluir aluno
6 - Registrar entrada
7 - Consultar frequência
0 - Sair

========================================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()

        elif opcao == "2":
            listar()

        elif opcao == "3":
            buscar()

        elif opcao == "4":
            editar()

        elif opcao == "5":
            excluir()
            
        elif opcao == "6":
            registrar_entrada()

        elif opcao == "7":
            consultar_frequencia()
            
        elif opcao == "0":
            print("\nSistema encerrado.")
            break

        else:
            print("\nOpção inválida.")

def editar():
    print("\n========== EDITAR ALUNO ==========")

    try:
        id_aluno = int(input("Digite a matrícula do aluno: "))
    except ValueError:
        print("Matrícula inválida.")
        return

    aluno = banco.buscar_aluno(id_aluno)

    if aluno is None:
        print("\nAluno não encontrado.")
        return

    print("\nDeixe o campo vazio para manter a informação atual.")

    nome = input(f"Nome [{aluno[1]}]: ")
    idade = input(f"Idade [{aluno[2]}]: ")
    telefone = input(f"Telefone [{aluno[3]}]: ")
    email = input(f"E-mail [{aluno[4]}]: ")
    plano = input(f"Plano [{aluno[5]}]: ")
    valor = input(f"Valor do plano [{aluno[6]}]: ")

    if nome == "":
        nome = aluno[1]

    if idade == "":
        idade = aluno[2]
    else:
        try:
            idade = int(idade)
        except ValueError:
            print("Idade inválida.")
            return

    if telefone == "":
        telefone = aluno[3]

    if email == "":
        email = aluno[4]

    if plano == "":
        plano = aluno[5]

    if valor == "":
        valor = aluno[6]
    else:
        try:
            valor = float(valor.replace(",", "."))
        except ValueError:
            print("Valor inválido.")
            return

    banco.editar_aluno(
        id_aluno,
        nome,
        idade,
        telefone,
        email,
        plano,
        valor
    )

    print("\nAluno atualizado com sucesso!")


def excluir():
    print("\n========== EXCLUIR ALUNO ==========")

    try:
        id_aluno = int(input("Digite a matrícula do aluno: "))
    except ValueError:
        print("Matrícula inválida.")
        return

    aluno = banco.buscar_aluno(id_aluno)

    if aluno is None:
        print("\nAluno não encontrado.")
        return

    print(f"\nAluno: {aluno[1]}")

    confirmacao = input(
        "Tem certeza que deseja excluir? (s/n): "
    ).lower()

    if confirmacao == "s":
        banco.excluir_aluno(id_aluno)
        print("\nAluno excluído com sucesso!")
    else:
        print("\nExclusão cancelada.")
def registrar_entrada():
    print("\n========== REGISTRAR ACESSO ==========")

    try:
        id_aluno = int(input("Digite a matrícula do aluno: "))
    except ValueError:
        print("Matrícula inválida.")
        return

    aluno = banco.buscar_aluno(id_aluno)

    if aluno is None:
        print("\nAluno não encontrado.")
        return

    if aluno[7] != "Ativo":
        print("\nO aluno não está ativo.")
        return

    frequencia.registrar_acesso(id_aluno)

    print(f"""
Acesso registrado com sucesso!

Aluno: {aluno[1]}
Matrícula: {aluno[0]}
""")

def consultar_frequencia():
    print("\n========== HISTÓRICO DE ACESSOS ==========")

    registros = frequencia.listar_frequencia()

    if not registros:
        print("Nenhum acesso registrado.")
        return

    for registro in registros:
        print(f"""
Registro: {registro[0]}
Matrícula: {registro[1]}
Aluno: {registro[2]}
Data: {registro[3]}
Horário: {registro[4]}
------------------------------------------
""")

menu()