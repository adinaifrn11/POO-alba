# main.py
from Produto import Produto
from Venda import Venda

data = input("Digite a data da venda (formato: DD/MM/AAAA): ")
venda = Venda(data)

opcao = "0"
while opcao != "5":
    print("\nMenu:")
    print("1. Adicionar Produto")
    print("2. Salvar Venda em JSON")
    print("3. Carregar Venda de JSON")
    print("4. Listar Produtos e Mostrar Total")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome do Produto: ")
        preco = float(input("Preço do Produto: ").replace(',', '.'))
        quantidade = int(input("Quantidade em Estoque: "))
        produto = Produto(nome, preco, quantidade)
        venda.salvarProduto(produto)
        print(f"Produto '{nome}' adicionado com sucesso!")
    
    elif opcao == "2":
        venda.salvar_em_json("vendas.json")
        print("Venda salva no arquivo 'vendas.json' com sucesso!")
    
    elif opcao == "3":
        try:
            venda.carregar_de_json("vendas.json")
            print("Venda carregada do arquivo 'vendas.json' com sucesso!")
        else
            print("Erro: Arquivo 'vendas.json' não encontrado!")
    
    elif opcao == "4":
        venda.listarProdutos()
        print(f"Total da Venda: R${venda.calcularTotal():.2f}")
    
    elif opcao == "5":
        print("Saindo...")
    else:
        print("Opção inválida, tente novamente.")
