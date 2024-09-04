from produto import Produto
from venda import Venda

def menu():
    venda = Venda("04/09/2024")
    
    while True:
        print("===== Menu de Vendas =====")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Calcular total da venda")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade: "))
            produto = Produto(nome, preco, quantidade)
            venda.adicionar_produto(produto)
            print(f"Produto {nome} adicionado com sucesso!")

        elif opcao == '2':
            nome = input("Nome do produto a remover: ")
            venda.remover_produto(nome)
            print(f"Produto {nome} removido com sucesso!")

        elif opcao == '3':
            produtos = venda.get_produtos()
            if produtos:
                print("\nProdutos na venda:")
                for produto in produtos:
                    print(f"- {produto.get_nome()} | Preço: {produto.get_preco()} | Quantidade: {produto.get_quantidade()}")
            else:
                print("Nenhum produto na venda.")

        elif opcao == '4':
            total = venda.calcular_total()
            print(f"Total da venda: R$ {total:.2f}")

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
