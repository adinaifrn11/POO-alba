from conta_bancaria import conta_bancaria
class conta_poupança:
    def __init__(self,rendimento,ver_rendimento,render):
        self.rendimento = rendimento
        self.ver_rendimento = ver_rendimento
        self.render = render

    def render(self):
        valor_rendimento = self.saldo * self.rendimento
        self.saldo += valor_rendimento
        return f"Rendimento de R${valor_rendimento:.2f}Novo saldo: R${self.saldo:.2f}"

    def ver_rendimento(self):
     return f"Taxa de rendimento: {self.rendimento * 150:.2f}%"

    