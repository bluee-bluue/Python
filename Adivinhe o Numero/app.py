import random
import os


def sortear(min, max):
    sorteado = random.randint(int(min), int(max))
    return sorteado

def compara(num_escolhido, num_sorteado):
    resultado = False
    if num_escolhido > num_sorteado:
        os.system("cls")
        print("Errou! Tente novamente.")
    elif num_escolhido < num_sorteado:
        os.system("cls")
        print("Errou! Tente novamente.")
    elif num_escolhido == num_sorteado:
        os.system("cls")
        print("Parabens!!! Você acertou.")
        resultado = True
    return resultado


def main():
    sorteado = int(sortear(1, 10))
    numeros_errados = []
    while True:
        try:
            numeroEscolhido = int(input("Digite um número: "))
            comparacao = compara(numeroEscolhido, sorteado)

            if comparacao == False:
                numeros_errados.append(numeroEscolhido)
                print("Números errados:", numeros_errados)
            elif comparacao == True:
                break
        except:
            print("Resposta invalida!")


if __name__ == "__main__":
    main()
