from dados.banco import conectar
def consultar_agendamentos():
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n===== CONSULTA DE AGENDAMENTOS =====")
    print("1 - Consultar pelo CPF do cliente")
    print("2 - Consultar pela data")
    print("3 - Alterar status do agendamento")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cpf = input("Digite o CPF do cliente: ")

        cursor.execute("""
        SELECT a.id, c.nome, s.nome, p.nome,
        a.data, a.horario, a.status
        FROM agendamentos a
        JOIN clientes c ON a.cliente_id = c.id
        JOIN servicos s ON a.servico_id = s.id
        JOIN profissionais p ON a.profissional_id = p.id
        WHERE c.cpf = ?
        ORDER BY a.data, a.horario
        """, (cpf,))

    elif opcao == "2":
        data = input("Digite a data (DD/MM/AAAA): ")

        try:
            from datetime import datetime
            data = datetime.strptime(data, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            print("Data inválida.")
            conexao.close()
            return

        cursor.execute("""
        SELECT a.id, c.nome, s.nome, p.nome,
        a.data, a.horario, a.status
        FROM agendamentos a
        JOIN clientes c ON a.cliente_id = c.id
        JOIN servicos s ON a.servico_id = s.id
        JOIN profissionais p ON a.profissional_id = p.id
        WHERE a.data = ?
        ORDER BY a.horario
        """, (data,))

    elif opcao == "3":
        id_agendamento = input("Número do agendamento: ")

        cursor.execute(
            "SELECT id FROM agendamentos WHERE id = ?",
            (id_agendamento,)
        )

        agendamento = cursor.fetchone()

        if agendamento is None:
            print("Agendamento não encontrado.")
            conexao.close()
            return

        print("1 - Pendente")
        print("2 - Confirmado")
        print("3 - Concluído")
        print("4 - Cancelado")

        status_opcao = input("Escolha o novo status: ")

        status = {
            "1": "Pendente",
            "2": "Confirmado",
            "3": "Concluído",
            "4": "Cancelado"
        }

        if status_opcao not in status:
            print("Opção inválida.")
            conexao.close()
            return

        cursor.execute(
            "UPDATE agendamentos SET status = ? WHERE id = ?",
            (status[status_opcao], id_agendamento)
        )

        conexao.commit()
        print("Status atualizado com sucesso!")
        conexao.close()
        return

    else:
        print("Opção inválida.")
        conexao.close()
        return

    resultados = cursor.fetchall()

    if not resultados:
        print("Nenhum agendamento encontrado.")
    else:
        for agendamento in resultados:
            print("\nNúmero:", agendamento[0])
            print("Cliente:", agendamento[1])
            print("Serviço:", agendamento[2])
            print("Profissional:", agendamento[3])
            print("Data:", agendamento[4])
            print("Horário:", agendamento[5])
            print("Status:", agendamento[6])

    conexao.close()
