class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0
        self.limite_saque_diario = 3
        self.valor_max_saque = 1000.0
        self.total_sacado_hoje = 0.0
        self.limite_diario = 5000.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            print(f"Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito inválido. Deve ser maior que zero.")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saque_diario:
            print("Limite de saques diários atingido.")
            return
        
        if valor > self.valor_max_saque:
            print(f"O valor máximo por saque é R${self.valor_max_saque:.2f}.")
            return
        
        if self.total_sacado_hoje + valor > self.limite_diario:
            print(f"Limite de saque diário de R${self.limite_diario:.2f} atingido.")
            return
        
        if valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
            return
        
        if valor > 0:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_diarios += 1
            self.total_sacado_hoje += valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            print(f"Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de saque inválido. Deve ser maior que zero.")
    
    def exibir_extrato(self):
        print("Extrato:")
        for deposito in self.depositos:
            print(f"Depósito: R${deposito:.2f}")
        for saque in self.saques:
            print(f"Saque: R${saque:.2f}")
        print(f"Saldo atual: R${self.saldo:.2f}")

    def resetar_saque_diario(self):
        self.saques_diarios = 0
        self.total_sacado_hoje = 0.0


def main():
    banco = Banco()

    while True:
        print("\nEscolha uma operação:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            valor = float(input("Digite o valor do depósito: R$"))
            banco.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: R$"))
            banco.sacar(valor)
        elif opcao == '3':
            banco.exibir_extrato()
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


if __name__ == "__main__":
    main()
