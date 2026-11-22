from dados.banco import conectar
def cadastrar_profissional():
    conexao = conectar()
    cursor = conexao.cursor()
    print("\n===== CADASTRO DE PROFISSIONAL=====")
    nome= input("Nome do Profissional: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    cursor.execute("INSERT INTO profissional(nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conexao.commit()
    print("Profissional cadastrado com sucesso!")
    conexao.close()
