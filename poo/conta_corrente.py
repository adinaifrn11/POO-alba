from conta_bancaria import conta_bancaria
class conta_corrente :
    def __init__(self,titular,cpf,saldo,numerocc):
         super(). __init__(self,titular,cpf,saldo)
         self.numerocc = numerocc

    def mostrarcc(self):
        return f"Titular: {self.titular}CPF: {self.cpf}Saldo: R${self.saldo:.2f}Número da Conta Corrente: {self.numerocc}"