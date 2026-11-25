from modulos.clientes import cadastrar_cliente
from modulos.servicos import cadastrar_servico
from modulos.profissionais import cadastrar_profissional
from modulos.especialidades import cadastrar_especialidades
from modulos.agendamentos import cadastrar_agendamento


while True:
    print("\n" + "=" * 40)
    print("             AgendaFácil")
    print("       Sistema de Agendamento")
    print("=" * 40)

    print("1 - Cadastro de clientes")
    print("2 - Cadastro de serviços")
    print("3 - Cadastro de profissionais")
    print("4 - Agendamentos")
    print("5 - Consultas e histórico")
    print("6 - Cadastro de especialidades")
    print("0 - Sair")
    print("=" * 40)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        cadastrar_servico()

    elif opcao == "3":
        cadastrar_profissional()

    elif opcao == "4":
        cadastrar_agendamento()

    elif opcao == "5":
        print("Módulo de consultas e histórico")

    elif opcao == "6":
        cadastrar_especialidades()

    elif opcao == "0":
        print("Sistema AgendaFácil encerrado.")
        break

    else:
        print("Opção inválida! Tente novamente.")



