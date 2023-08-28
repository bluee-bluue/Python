import os

lista_de_tarefas = []


def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    lista_de_tarefas.append(tarefa)
    os.system("cls")
    print("Tarefa adicionada com sucesso!")


def mostrar_tarefas():
    i = 1
    if lista_de_tarefas:
        print("Lista de tarefas:")
        for tarefa in lista_de_tarefas:
            print(f"{i}. {tarefa}")
            i += 1
    else:
        os.system("cls")
        print("Não há tarefas na lista.")


def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar tarefa")
        print("2. Mostrar tarefas")
        print("3. Sair")

        opcao = input("\nDigite o número da opção desejada: ")

        match opcao:
            case "1":
                os.system("cls")
                adicionar_tarefa()
            case "2":
                os.system("cls")
                mostrar_tarefas()
            case "3":
                os.system("cls")
                print("Saindo do programa.")
                break
            case _:
                os.system("cls")
                print("Opção inválida. Digite novamente.")


if __name__ == "__main__":
    main()
