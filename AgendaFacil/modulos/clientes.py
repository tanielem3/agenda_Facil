from dados.banco import conectar
def cadastrar_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    print("\n===== CADASTRO DE CLIENTE =====")
    nome = input("Nome completo: ")
    cpf = input("CPF: ")
    email = input("E-mail: ")
    telefone = input("telefone: ")

    print("\n===== CONFIRMAÇÃO DE CADASTRO =====")
    print("Nome completo:", nome)
    print("CPF:", cpf)
    print("E-mil:", email)
    print("Telefne:", telefone)
    cursor.execute("INSERT INTO clientes(nome, cpf, email, telefone) VALUES (?, ?, ?, ?)", (nome, cpf, email, telefone))
    conexao.commit()
    print("Cliente cadastrado com sucesso!")
    conexao.close()


