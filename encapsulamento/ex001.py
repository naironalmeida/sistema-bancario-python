class Conta:
    def __init__(self, titular, saldo, numero):
        self.titular = titular
        self._saldo = saldo
        self.numero = numero

    def depositar(self, valor):
        if valor <= 0:
            return "O valor para depósito deve ser maior que zero."
        else:
            self._saldo += valor
            return f"Valor depositado: R${valor:.2f}"

    def sacar(self, valor):
        if valor <= 0:
            return "O valor do saque deve ser maior que zero."

        if valor > self._saldo:
            return "Saldo insuficiente."

        self._saldo -= valor
        return f"Valor do saque: R${valor:.2f}"

    def exibir_dados(self):
        return (
            f"Titular da conta: {self.titular} | "
            f"Saldo da conta: R${self._saldo:.2f} | "
            f"Número da conta: {self.numero}"
        )



conta = Conta("Nairon", 0, 12345)


while True:
    print("\n=== SISTEMA DE CONTA BANCÁRIA ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Mostrar Dados")
    print("4 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor que deseja depositar: "))

        print(conta.depositar(valor))

        print(f"Saldo atual: R${conta._saldo:.2f}")

    elif opcao == "2":
        valor = float(input("Digite o valor que deseja sacar: "))

        print(conta.sacar(valor))

        print(f"Saldo atual: R${conta._saldo:.2f}")

    elif opcao == "3":
        print(conta.exibir_dados())

    elif opcao == "4":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")