# AgendaFácil

Sistema simples de agendamento de serviços para um estabelecimento de beleza, desenvolvido em Python e SQLite como Projeto Integrador do curso de Análise e Desenvolvimento de Sistemas.

## Tecnologias utilizadas

- Python 3
- SQLite (biblioteca `sqlite3`, incluída na instalação padrão do Python)
- Visual Studio Code (ambiente recomendado para edição e execução)

## Estrutura do projeto

O código da aplicação está na pasta `AgendaFacil`:

- `main.py`: arquivo principal e menu do sistema.
- `dados/banco.py`: conexão com o SQLite e criação das tabelas.
- `modulos/`: funcionalidades de clientes, serviços, profissionais, especialidades, agendamentos e consultas.

O arquivo do banco de dados `dados/agenda.db` é criado localmente quando o sistema é iniciado. Por isso, ele pode não aparecer no repositório antes da primeira execução.

## Como executar pelo Visual Studio Code

1. Instale o **Python 3** no computador, caso ainda não esteja instalado.
2. Instale o **Visual Studio Code**.
3. No VS Code, instale a extensão **Python**, publicada pela Microsoft.
4. Abra o repositório no VS Code: **Arquivo > Abrir Pasta** e selecione a pasta do projeto baixada do GitHub.
5. Abra o terminal integrado em **Terminal > Novo Terminal**.
6. No terminal, entre na pasta da aplicação:

   ```bash
   cd AgendaFacil
   ```

7. Execute o programa:

   **Windows:**
   ```bash
   py main.py
   ```

   **Linux ou macOS:**
   ```bash
   python3 main.py
   ```

   Se o comando `python` estiver configurado no computador, também pode ser utilizado `python main.py`.

8. O menu do AgendaFácil será exibido no terminal. Digite o número da opção desejada e pressione **Enter**. Para encerrar, escolha a opção **0 - Sair**.

## Banco de dados

Na inicialização, o programa chama a função que cria as tabelas necessárias no SQLite. O banco é armazenado localmente em `AgendaFacil/dados/agenda.db`. Não é necessário instalar ou iniciar um servidor de banco de dados separado.

## Observações

- Execute o arquivo `main.py` estando dentro da pasta `AgendaFacil`, para que as importações dos módulos funcionem corretamente.
- Não é necessário instalar pacotes externos para executar a versão atual do sistema.
- Os dados cadastrados ficam no arquivo local `agenda.db`. Faça uma cópia desse arquivo se precisar preservar os registros de uma instalação.
