import random
import json
import time
import os

perguntas = {}

with open("Perguntas e Respostas/perguntas.json", "r") as arquivo:
    perguntas = json.load(arquivo)

def obter_pergunta():
    if perguntas:
        pergunta_escolhida = random.choice(perguntas)
        perguntas.remove(pergunta_escolhida)
        return(pergunta_escolhida)
    else:
        return None

def main():
    pontuacao = 0
    while True:
        os.system("cls")
        pergunta = obter_pergunta()
        
        if pergunta is None:
            print(f"Fim de jogo! sua pontuação final foi de: {pontuacao} pontos")
            break

        print(f"Sua pontuação atual é: {pontuacao} pontos\n")
        print(pergunta["pergunta"])
        resposta = input("\nDigite apenas a alternativa: ").upper()

        if resposta == pergunta["resposta"]:
            os.system("cls")
            print("Resposta Correta!")
            pontuacao += 10
            time.sleep(1)
        else:
            os.system("cls")
            print("Resposta incorreta!")
            time.sleep(1)

if __name__ == "__main__":
    main()