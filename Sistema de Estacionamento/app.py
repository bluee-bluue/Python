from Models.estacionamento import Estacionamento

precoInicial = 0
precoPorHora = 0

precoInicial = input(
    "Seja bem vindo ao sistema de estacionamento!\n" + "Digite o preço inicial: "
)

precoPorHora = input("Digite o preço por hora: ")

estacionamento = Estacionamento(precoInicial, precoPorHora)

while True:
    print("\nEscolha uma opção:")
    print("1. Cadastrar veículo")
    print("2. Remover veículo")
    print("3. Listar veículos")
    print("4. Sair")

    opcao = input("\nDigite o número da opção desejada: ")

    match opcao:
        case "1":
            estacionamento.adicionarVeiculos()
        case "2":
            estacionamento.removerVeiculos()
        case "3":
            estacionamento.listarVeiculos()
        case "4":
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Digite novamente.")
