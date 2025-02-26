produtos=[]

def cadastrar ():
    nome=input("Digite o nome do produto: ")
    marca=input("Digite a marca do produto: ")
    codigo=input("Digite o codigo do produto: ")
    quantidade=input("Digite a quantidade do produto: ")
    preco=input("Digite o preço do produto: ")
    
    produto={"nome":nome, "marca":marca,"codigo":codigo,"quantidade":quantidade,"preço":preco}
    produtos.append(produto)
    
    print(f"\nProduto {nome} cadastrado com sucesso.")
    
cadastrar() 
