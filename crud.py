produtos=[]

def cadastrar ():
    nome=input("Digite o nome do produto: ")
    marca=input("Digite a marca do produto: ")
    codigo=input("Digite o codigo do produto: ")
    quantidade=input("Digite a quantidade do produto: ")
    preco=input("Digite o preço do produto: ")
    
    produto={"nome":nome, "marca":marca,"codigo":codigo,"quantidade":quantidade,"preço":preco}
    produtos.append(produto)
    
    print(f"\nProduto [{nome} {marca}] cadastrado com sucesso.")
    

def listar ():
    print("Produtos cadastrados:\n")
    for produto in produtos:
        print(f"Nome: {produto["nome"]} - Marca: {produto["marca"]} - Codigo: {produto["codigo"]} - Quantidade: {produto["quantidade"]} - Preço: {produto["preço"]}")


def deletar ():
    codigo=input("Digite o codigo do produto que você deseja excluir: ")
    
    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print(f"\nProduto [{produto["nome"]} {produto["marca"]}] removido com sucesso")
            return
    
    print(f"Produto com codigo {codigo} não encontrado.")


def menu ():
    while True:
        print("\n" ,"-" * 50)
        print("========== MENU ==========")
        print("1 - Cadastrar produtos")
        print("2 - Listar produtos")
        print("3 - Deletar produto")
        print("0 - sair")
                
        opcao=input("\nEscolha uma opção: ")
        print("-" * 50)
        
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            deletar()
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Digite uma opção valida. Tente novamente.")
        

menu()