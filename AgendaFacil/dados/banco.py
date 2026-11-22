import sqlite3
from pathlib import Path
CAMINHO_BANCO = Path(__file__).resolve().parent.parent / "dados" / "agenda.db"

def conectar():
    conexao = sqlite3.connect(CAMINHO_BANCO)
    return conexao

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        email TEXT  NUL,
        telefone TEXT NOT NULL
        )
""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS servicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        duracao INTEGER NOT NULL,
        preco REAL NOT NULL
        )
""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profissionais(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT  NULL
    )

""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS especialidades(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome  TEXT NOT NULL UNIQUE
    )
""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profissional_especialidades(
    profissional_id INTEGER NOT NULL,
    especialidade_id INTEGER NOT NULL,
    FOREIGN KEY (profissional_id) REFERENCES profissionais(id),
    FOREIGN KEY (especialidade_id) REFERENCES especialidades(id),
    PRIMARY KEY (profissional_id, especialidade_id)
    )

""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NOT NULL,
        servico_id INTEGER NOT NULL,
        profissional_id INTEGER NOT NULL,
        data TEXT NOT NULL,
        horario TEXT NOT NULL,
        duracao INTEGER NOT NULL,
        status TEXT NOT NULL DEFAULT 'Pendente',
        FOREIGN KEY (cliente_id) REFERENCES clientes(id),
        FOREIGN KEY (servico_id) REFERENCES servicos(id),
        FOREIGN KEY (profissional_id) REFERENCES profissionais(id)
    )
    """)

    conexao.commit()
    conexao.close()

if  __name__ == "__main__":
    try:
        criar_tabelas()

        conexao = conectar()
        print("Banco de dados conectado com sucesso!")
        conexao.close()


    except sqlite3.Error as erro:
        print("Erro ao conectar o banco de dados", erro)
