from dados.banco import conectar
def cadastrar_servico():
    conexao = conectar()
    cursor = conexao.cursor()
    print("\n===== CADASTRO DE SERVIÇO=====")
    nome = input("Nome do serviço: ")
    preco = float(input("Preço do serviço:").replace("," "."))
    duracao = 60
    cursor.execute("INSERT INTO servicos(nome, preco, duracao) VALUES (?, ?, ?)", (nome, preco, duracao))
    conexao.commit()
    print("Serviço cadastrado com sucesso!")
    conexao.close()