class Main:
  pass


print("Testando fluxo de controle")

from cliente import cliente

from conta import Conta

c1 = cliente("João", "114400-2222")
conta = Conta(c1.nome, 6565, 0)

print(conta.titular, "Numero: ", conta.numero, "Seu Saldo", conta.saldo)
