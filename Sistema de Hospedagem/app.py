from Models.pessoa import Pessoa
from Models.reserva import Reserva
from Models.suite import Suite

hospedes = []

p1 = Pessoa("Caique")
p2 = Pessoa("João")

hospedes.append(p1)
hospedes.append(p2)

suite = Suite("Premium", 3, 30)

reserva = Reserva(15)
reserva.cadastrarSuite(suite)
reserva.cadastrarHospedes(hospedes)

print(f"Hóspedes: {reserva.obterQuantidadeHospedes()}")
print(f"Valor da diária: {reserva.calcularValorDiaria()}")
