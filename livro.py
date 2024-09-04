from autor import Autor

class Livro:
    def __init__(self, titulo , autor: Autor, anoPublicacao: int ):
        self.__titulo = titulo
        self.__autor = autor
        self.__anoPublicacao = anoPublicacao


    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor: Autor):
        self.__autor = autor

    def get_anoPublicacao(self):
        return self.__anoPublicacao

    def set_anoPublicacao(self, anoPublicacao: int):
        self.__anoPublicacao = anoPublicacao

    def exibirLivro(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor.get_nome()}")
        print(f"Ano de Publicação: {self.__anoPublicacao}")
