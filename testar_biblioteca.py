from biblioteca import Biblioteca
from livro import Livro
from autor import Autor

def exibir_menu():
    print("Menu da Biblioteca")
    print("1. Adicionar Livro")
    print("2. Remover Livro")
    print("3. Buscar Livro")
    print("4. Listar Livros")
    print("5. Sair")

def main():
    biblioteca = Biblioteca()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título do livro: ")
            nome_autor = input("Nome do autor: ")
            nacionalidade = input("Nacionalidade do autor: ")
            dataNascimento = input("Data de nascimento do autor: ")
            anoPublicacao = int(input("Ano de publicação: "))
            
            autor = Autor(nome_autor, nacionalidade, dataNascimento)
            livro = Livro(titulo, autor, anoPublicacao)
            biblioteca.adicionarLivro(livro)

        elif opcao == '2':
            titulo = input("Título do livro a ser removido: ")
            biblioteca.removerLivro(titulo)

        elif opcao == '3':
            titulo = input("Título do livro a ser buscado: ")
            livro = biblioteca.buscarLivro(titulo)
            if livro:
                livro.exibirLivro()

        elif opcao == '4':
            biblioteca.listarLivros()

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()