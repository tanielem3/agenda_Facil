from modulos.clientes import cadastrar_cliente
while True:
   #Aqui ficará exibido o menu
   print("=" * 40)
   print("         AgendaFácil")
   print("      Sistema de Agendamento")
   print("=" *40)

   print("\n1 - Cadasrao de clinte")
   print("2 - Cadastro do serviço")
   print("3 - Cadastro de profissionais")
   print("4 - Agendamentos")
   print("5 - Consultas e histórico ")
   print("0 - Sair")
   print("=" *40)

   opcao = input("Escolha uma opção: ")
   if opcao == "1":
      cadastrar_cliente()
   elif opcao == "2":
      print("Cadastro de serviços")
   elif opcao == "3":
      print("Cadastro de profissional")
   elif opcao == "4":
      print("Agendamentos")
   elif opcao == "5":
      print("Consultas e histórico")
   elif opcao == "0":
      print("Sistema AgendaFácil encerrado.")
      break
   else:
      print("Opçõ inválida! Tente novamente")



