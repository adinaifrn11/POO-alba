from produto import Produto
from produto import produto

class Venda:
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

    def set_total(self, total):
        self.__total = total

    def adicionar_produto(self, produto: Produto):
        self.__produtos.produto 

    def remover_produto(self, prduto: produto):
        self.__produtos.produto

    def calcular_total(self,produto: produto):
        self.__produtos = ("get_preço * get_quantidade = produtos")

