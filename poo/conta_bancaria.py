class Conta_bancaria:
    def __init__(self, titular, cpf, saldo=0):
        self.titular = titular
        self.cpf = cpf
        self.saldo = saldo

    def mostra_conta(self):
        return f"Titular: {self.titular}, CPF: {self.cpf}, Saldo: R${self.saldo:.2f}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso! Saldo atual: R${self.saldo:.2f}"
        else:
            return "Valor de depósito inválido!"

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso! Saldo atual: R${self.saldo:.2f}"
        else:
            return "Saldo insuficiente ou valor inválido para saque!"

    def verificar_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"


class Conta_corrente(Conta_bancaria):
    def __init__(self, titular, cpf, saldo=0, numerocc=None):
        super().__init__(titular, cpf, saldo)
        self.numerocc = numerocc

    def mostrarcc(self):
        return f"Titular: {self.titular}, CPF: {self.cpf}, Número da Conta Corrente: {self.numerocc}, Saldo: R${self.saldo:.2f}"


class Conta_poupanca(Conta_bancaria):
    def __init__(self, titular, cpf, saldo=0, rendimento=0.02):
        super().__init__(titular, cpf, saldo)
        self.rendimento = rendimento

    def ver_rendimento(self):
        return f"Rendimento atual: {self.rendimento * 100:.2f}% ao mês"

    def render(self):
        self.saldo += self.saldo * self.rendimento
        return f"Rendimento aplicado! Saldo atual: R${self.saldo:.2f}"


def criar_conta_corrente(contas):
    titular = input("Nome do titular: ")
    cpf = input("CPF do titular: ")
    numerocc = input("Número da conta corrente: ")
    contas[cpf] = Conta_corrente(titular, cpf, numerocc=numerocc)
    return "Conta Corrente criada com sucesso!"


def criar_conta_poupanca(contas):
    titular = input("Nome do titular: ")
    cpf = input("CPF do titular: ")
    contas[cpf] = Conta_poupanca(titular, cpf)
    return "Conta Poupança criada com sucesso!"


def depositar(contas):
    cpf = input("Informe o CPF do titular: ")
    if cpf in contas:
        valor = float(input("Valor a ser depositado: R$"))
        return contas[cpf].depositar(valor)
    else:
        return "Conta não encontrada!"


def sacar(contas):
    cpf = input("Informe o CPF do titular: ")
    if cpf in contas:
        valor = float(input("Valor a ser sacado: R$"))
        return contas[cpf].sacar(valor)
    else:
        return "Conta não encontrada!"


def verificar_saldo(contas):
    cpf = input("Informe o CPF do titular: ")
    if cpf in contas:
        return contas[cpf].verificar_saldo()
    else:
        return "Conta não encontrada!"


def ver_rendimento(contas):
    cpf = input("Informe o CPF do titular: ")
    if cpf in contas and isinstance(contas[cpf], Conta_poupanca):
        return contas[cpf].ver_rendimento()
    else:
        return "Conta Poupança não encontrada!"


def aplicar_rendimento(contas):
    cpf = input("Informe o CPF do titular: ")
    if cpf in contas and isinstance(contas[cpf], Conta_poupanca):
        return contas[cpf].render()
    else:
        return "Conta Poupança não encontrada!"


def menu(contas):
    while True:
        print("\nMenu:")
        print("1. Criar Conta Corrente")
        print("2. Criar Conta Poupança")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Verificar Saldo")
        print("6. Verificar Rendimento (Poupança)")
        print("7. Aplicar Rendimento (Poupança)")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print(criar_conta_corrente(contas))

        elif opcao == '2':
            print(criar_conta_poupanca(contas))

        elif opcao == '3':
            print(depositar(contas))

        elif opcao == '4':
            print(sacar(contas))

        elif opcao == '5':
            print(verificar_saldo(contas))

        elif opcao == '6':
            print(ver_rendimento(contas))

        elif opcao == '7':
            print(aplicar_rendimento(contas))

        elif opcao == '8':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    contas = {}  
    menu(contas)