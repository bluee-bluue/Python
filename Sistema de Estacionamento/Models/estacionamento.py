class Estacionamento:
    def __init__(self, precoInicial, precoPorHora):
        self.precoInicial = precoInicial
        self.precoPorHora = precoPorHora
        self.veiculos = []

    def adicionarVeiculos(self):
        placa = input("Digite a placa do veículo para estacionar: ")
        self.veiculos.append(placa)

    def removerVeiculos(self):
        placa = input("Digite a placa do veículo para remover: ")

        if any(x.upper() == placa.upper() for x in self.veiculos):
            horas = int(input("Digite a quantidade de horas que o veículo permaneceu estacionado: "))
            valorTotal = int(self.precoInicial) + int(self.precoPorHora) * horas
            self.veiculos.remove(placa)
            print(f"O veículo da placa {placa} foi removido e o preço total foi de: R${valorTotal:.2f}")
        else:
            print("Desculpe, esse veículo não está estacionado aqui. Confira se digitou a placa corretamente")

    def listarVeiculos(self):
        if self.veiculos:
            print("Os veículos estacionados são:")
            for i in self.veiculos:
                print(i)
        else:
            print("Não há veículos estacionados.")
