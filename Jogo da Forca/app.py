import random
import os

palavras = [
    "COMPUTADOR", "MONITOR", "PYTHON", "VSCODE", "TERMINAL",
    "PLACA MAE", "MEMORIA RAM", "PLACA DE VIDEO", "JAVA",
    "PROCESSADOR", "DISCO RIGIDO", "CELULAR"
]

def main():
    palavraSorteada = random.choice(palavras).upper()
    palavraMudada = ["_" if letra != " " else " " for letra in palavraSorteada]
    tentativas_erradas = []
    tentativas_maximas = 6

    while True:
        os.system("cls")
        print("Palavra:", " ".join(palavraMudada))
        print("Tentativas erradas:", ", ".join(tentativas_erradas))
        letraEscolhida = input("Digite uma letra: ").upper()

        if letraEscolhida.isalpha() and len(letraEscolhida) == 1:
            if letraEscolhida in palavraSorteada:
                for i in range(len(palavraSorteada)):
                    if palavraSorteada[i] == letraEscolhida:
                        palavraMudada[i] = letraEscolhida
            else:
                tentativas_erradas.append(letraEscolhida)

        if "_" not in palavraMudada:
            print("Parabéns! Você ganhou! A palavra era:", palavraSorteada)
            break

        if len(tentativas_erradas) >= tentativas_maximas:
            print("Você perdeu! A palavra era:", palavraSorteada)
            break

if __name__ == "__main__":
    main()
