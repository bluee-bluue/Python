import os

numeros = []


def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Média")
        print("6. Sair")

        opcao = input("\nDigite o número da opção desejada: ")

        match opcao:
            case "1":
                os.system("cls")
                comeco()
                adicao()
            case "2":
                os.system("cls")
                comeco()
                subtracao()
            case "3":
                os.system("cls")
                comeco()
                multiplicacao()
            case "4":
                os.system("cls")
                comeco()
                divisao()
            case "5":
                os.system("cls")
                Media()
            case "6":
                os.system("cls")
                print("Saindo do programa.")
                break
            case _:
                os.system("cls")
                print("Opção inválida. Digite novamente.")


def comeco():
    quantidade = input("Digite a quantidade: ")
    i = 0
    numeros.clear()

    while i < int(quantidade):
        numero = input(f"Digite o {i+1}o número: ")
        numeros.append(numero)
        i += 1


def adicao():
    resultado = 0
    for n in numeros:
        resultado += int(n)

    print(f"A soma dos números é igual a {resultado}")


def subtracao():
    resultado = int(numeros[0])
    for n in numeros[1:]:
        resultado -= int(n)

    print(f"A subtração dos números é igual a {resultado}")


def multiplicacao():
    resultado = 1
    for n in numeros:
        resultado *= int(n)

    print(f"A multiplicação dos números é igual a {resultado}")


def divisao():
    resultado = int(numeros[0])
    for n in numeros[1:]:
        resultado /= int(n)

    print(f"A divisão dos números é igual a {resultado}")

def Media():
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
