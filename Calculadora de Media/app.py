import os

numeros = []


def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Calculardora")
        print("2. Sair")

        opcao = input("\nDigite o número da opção desejada: ")

        match opcao:
            case "1":
                os.system("cls")
                calcularMedia()
            case "2":
                os.system("cls")
                print("Saindo do programa.")
                break
            case _:
                os.system("cls")
                print("Opção inválida. Digite novamente.")


def calcularMedia():
    quantidade = input("Digite a quantidade: ")
    resultado = 0
    numeros.clear()
    i = 0

    while i < int(quantidade):
        numero = input(f"Digite o {i+1}o número: ")
        numeros.append(numero)
        i += 1

    for n in numeros:
        resultado += int(n)

    media = resultado / int(quantidade)

    print(f"\nA média dos números é igual a {media}")


if __name__ == "__main__":
    main()
