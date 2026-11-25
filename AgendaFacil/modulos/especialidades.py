
from dados.banco import conectar


def cadastrar_especialidades():
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n===== CADASTRO DE ESPECIALIDADE =====")
    nome = input("Nome da especialidade: ")

    cursor.execute(
        "INSERT INTO especialidades(nome) VALUES (?)",
        (nome,)
    )

    conexao.commit()
    print("Especialidade cadastrada com sucesso!")
    conexao.close()


def vincular_especialidade_profissional():
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n===== VINCULAR ESPECIALIDADE =====")

    cursor.execute("SELECT id, nome FROM profissionais")
    profissionais = cursor.fetchall()

    if not profissionais:
        print("Cadastre um profissional primeiro.")
        conexao.close()
        return

    print("\n===== PROFISSIONAIS =====")
    for profissional in profissionais:
        print(profissional[0], "-", profissional[1])

    id_profissional = int(input("Digite o número do profissional: "))

    cursor.execute(
        "SELECT id FROM profissionais WHERE id = ?",
        (id_profissional,)
    )
    profissional = cursor.fetchone()

    if profissional is None:
        print("Profissional não encontrado.")
        conexao.close()
        return

    cursor.execute("SELECT id, nome FROM especialidades")
    especialidades = cursor.fetchall()

    if not especialidades:
        print("Cadastre uma especialidade primeiro.")
        conexao.close()
        return

    print("\n===== ESPECIALIDADES CADASTRADAS =====")
    for especialidade in especialidades:
        print(especialidade[0], "-", especialidade[1])

    id_especialidade = int(input("Digite o número da especialidade: "))

    cursor.execute(
        "SELECT id FROM especialidades WHERE id = ?",
        (id_especialidade,)
    )
    especialidade = cursor.fetchone()

    if especialidade is None:
        print("Especialidade não encontrada.")
        conexao.close()
        return

    cursor.execute(
        """INSERT INTO profissional_especialidades
        (profissional_id, especialidade_id) VALUES (?, ?)""",
        (id_profissional, id_especialidade)
    )

    conexao.commit()
    print("Especialidade vinculada ao profissional com sucesso!")
    conexao.close()
