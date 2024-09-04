from livro import Livro

class Biblioteca:
    def __init__(self):
        self.__livros = []

    def adicionarLivro(self, livro):
        self.__livros.append(livro)
        print(f"Livro '{livro.get_titulo()}' adicionado à biblioteca.")

    def removerLivro(self, titulo):
        for livro in self.__livros:
            if livro.get_titulo() == titulo:
                self.__livros.remove(livro)
                print(f"Livro '{titulo}' removido da biblioteca.")
                return
        print(f"Livro '{titulo}' não encontrado.")

   
    def buscarLivro(self, titulo):
        for livro in self.__livros:
            if livro.get_titulo() == titulo:
                return livro
        print(f"Livro '{titulo}' não encontrado.")
        return None

    
    def listarLivros(self):
        if not self.__livros:
            print("A biblioteca está vazia.")
        else:
            print("Livros disponíveis na biblioteca:")
            for livro in self.__livros:
                livro.exibirLivro()
                print("-" * 30)