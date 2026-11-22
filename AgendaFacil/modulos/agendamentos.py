
from dados.banco import conectar
from datetime import datetime, timedelta


def cadastrar_agendamento():
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n===== CADASTRO DE AGENDAMENTO =====")

    cpf = input("CPF do cliente: ")
    cursor.execute("SELECT id, nome FROM clientes WHERE cpf = ?", (cpf,))
    cliente = cursor.fetchone()

    if cliente is None:
        print("Cliente não encontrado. Cadastre o cliente primeiro.")
        conexao.close()
        return

    print("Cliente encontrado:", cliente[1])

    cursor.execute("SELECT id, nome, duracao, preco FROM servicos")
    servicos = cursor.fetchall()

    print("\n===== SERVIÇOS DISPONÍVEIS =====")
    for servico in servicos:
        print(servico[0], "-", servico[1], "- R$", servico[3])

    id_servico = int(input("Digite o número do serviço desejado: "))
    cursor.execute(
        "SELECT id, nome, duracao, preco FROM servicos WHERE id = ?",
        (id_servico,)
    )
    servico_escolhido = cursor.fetchone()

    if servico_escolhido is None:
        print("Serviço não encontrado.")
        conexao.close()
        return

    print("Serviço escolhido:", servico_escolhido[1])
    print("Valor: R$", servico_escolhido[3])

    data_texto = input("Data do agendamento (DD/MM/AAAA): ")
    horario = input("Horário (HH:MM): ")

    try:
        data_agendamento = datetime.strptime(data_texto, "%d/%m/%Y")
        hora_inicio = datetime.strptime(horario, "%H:%M")
    except ValueError:
        print("Data ou horário inválido.")
        conexao.close()
        return

    if data_agendamento.weekday() == 6:
        print("O salão não funciona aos domingos.")
        conexao.close()
        return

    minutos = hora_inicio.hour * 60 + hora_inicio.minute
    duracao = servico_escolhido[2]

    if minutos < 480 or minutos % 30 != 0:
        print("O horário deve começar entre 08:00 e 18:00, em intervalos de 30 minutos.")
        conexao.close()
        return

    if minutos + duracao > 1080:
        print("O atendimento precisa terminar até as 18:00.")
        conexao.close()
        return

    data_banco = data_agendamento.strftime("%Y-%m-%d")

    cursor.execute("SELECT id, nome FROM profissionais")
    profissionais = cursor.fetchall()

    if not profissionais:
        print("Não existem profissionais cadastrados.")
        conexao.close()
        return

    print("\n===== PROFISSIONAIS DISPONÍVEIS =====")
    for profissional in profissionais:
        print(profissional[0], "-", profissional[1])

    id_profissional = int(input("Digite o número do profissional: "))

    cursor.execute(
        "SELECT id, nome FROM profissionais WHERE id = ?",
        (id_profissional,)
    )
    profissional_escolhido = cursor.fetchone()

    if profissional_escolhido is None:
        print("Profissional não encontrado.")
        conexao.close()
        return

    inicio_novo = hora_inicio.hour * 60 + hora_inicio.minute
    fim_novo = inicio_novo + duracao

    cursor.execute(
        """SELECT horario, duracao FROM agendamentos
        WHERE profissional_id = ? AND data = ? AND status != 'Cancelado'""",
        (id_profissional, data_banco)
    )
    horarios_ocupados = cursor.fetchall()

    for horario_ocupado, duracao_ocupada in horarios_ocupados:
        hora_ocupada = datetime.strptime(horario_ocupado, "%H:%M")
        inicio_ocupado = hora_ocupada.hour * 60 + hora_ocupada.minute
        fim_ocupado = inicio_ocupado + duracao_ocupada

        if inicio_novo < fim_ocupado and fim_novo > inicio_ocupado:
            print("Esse profissional já possui um agendamento nesse horário.")
            conexao.close()
            return

    cursor.execute(
        """INSERT INTO agendamentos
        (cliente_id, servico_id, profissional_id, data, horario, duracao, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            cliente[0],
            servico_escolhido[0],
            profissional_escolhido[0],
            data_banco,
            horario,
            duracao,
            "Pendente"
        )
    )

    conexao.commit()
    print("\nAgendamento cadastrado com sucesso!")
    print("Cliente:", cliente[1])
    print("Serviço:", servico_escolhido[1])
    print("Profissional:", profissional_escolhido[1])
    print("Data:", data_texto)
    print("Horário:", horario)
    print("Status: Pendente")

    conexao.close()
