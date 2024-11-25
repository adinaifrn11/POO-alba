  def __init__(self, dataVenda):
        self.__produtos = []
        self.__dataVenda = dataVenda
        self.__total = 0.0
    
    def get_produtos(self):
        return self.__produtos
    
    def get_dataVenda(self):
        return self.__dataVenda
    
    def get_total(self):
        return self.__total
    
    def set_dataVenda(self, dataVenda):
        self.__dataVenda = dataVenda
    
    def calcularTotal(self):
        total = 0.0
        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()
        self.__total = total
        return total
    
    def salvarProduto(self, produto):
        self.__produtos.append(produto)
    
    def listarProdutos(self):
        if not self.__produtos:
            print("Nenhum produto na venda.")
        else:
            print(f"\nProdutos na Venda do dia {self.__dataVenda}:")
            for produto in self.__produtos:
                print(f"Nome: {produto.get_nome()}, Preço: R${produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")
    
    def salvar_em_json(self, salvar_em_json):
        with open(salvar_em_json, 'w') as f:
            json.dump({
                "dataVenda": self.__dataVenda,
                "produtos": [{"nome": p.get_nome(), 
                              "preco": p.get_preco(), 
                              "quantidade": p.get_quantidade()} for p in self.__produtos],
                "total": self.__total
            }, f, ensure_ascii=False, indent=4)
    
    def carregar_de_json(self,carregar_de_json ):
        with open(carregar_de_json, 'r') as f:
            dados = json.load(f)
            self.__dataVenda = dados["dataVenda"]
            self.__produtos = [Produto(p["nome"], p["preco"], p["quantidade"]) for p in dados["produtos"]]
            self.__total = dados["total"]