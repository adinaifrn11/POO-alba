from Produto import Produto
from Venda import Venda
data = input("Digite a data da venda (formato: DD/MM/AAAA): ")
venda = Venda(data)
opcao = "0"
while opcao != "4":
    print("\nMenu:")
    print("1. Adicionar Produto")
    print("2. Salvar Produto")
    print("3. Remover Produto")
    print("4. Listar Produtos e Mostrar Total")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Nome do Produto: ")
        preco_valido = False
        while not preco_valido:
            preco = input("Preço do Produto: ")
            preco = preco.replace(',', '.')  # Substitui vírgulas por pontos
            pontos = 0
            for caractere in preco:
                if caractere == '.':
                    pontos += 1
            if pontos <= 1:
                partes = preco.split('.')
                valido = True
                for parte in partes:
                    if not parte.isdigit() and parte != '':
                        valido = False
                        break
                if valido:
                    preco = float(preco)
                    preco_valido = True
                else:
                    print("Preço inválido. Por favor, insira um valor numérico.")
            else:
                print("Preço inválido. Por favor, insira um valor numérico.")
        quantidade_valida = False
        while not quantidade_valida:
            quantidade = input("Quantidade em Estoque: ")
            if quantidade.isdigit():
                quantidade = int(quantidade)
                quantidade_valida = True
            else:
                print("Quantidade inválida. Por favor, insira um número inteiro.")
        produto = Produto(nome, preco, quantidade)
        venda.get_produtos().append(produto)
    elif opcao == "2":
     nome = input("Salvar Produto : ")
     preco = float(input("Digite o preço do produto: "))
     quantidade = int(input("Digite a quantidade do produto: "))
     produto = Produto(nome, preco, quantidade)
     venda.salvarProduto(produto)
     venda.salvar_em_json("vendas.json")
     print(f"Produto {nome} salvo e venda registrada no arquivo JSON.")
    
    elif opcao == "3":
        venda.listarProdutos()
        print(f"Total da Venda: R${venda.calcularTotal():.2f}")
    elif opcao == "4":
        print("Saindo...")
    else:
        print("Opção inválida, tente novamente.")